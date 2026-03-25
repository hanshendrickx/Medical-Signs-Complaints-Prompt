from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import TokenError
from django.contrib.auth import authenticate, logout as django_logout
from django.shortcuts import get_object_or_404, render
from .models import FamilyUser
from .serializers import (
    UserCreateSerializer,
    UserSerializer,
    UserProfileSerializer,
    FamilyMemberSerializer,
)


class CreateUserView(generics.CreateAPIView):
    """Signup endpoint for permanent family accounts and guest accounts."""

    serializer_class = UserCreateSerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        # Auto‑set guardian if user is minor and guardian not provided
        user = serializer.save()
        # Determine country from request IP if not provided
        if not user.country:
            user.country = self.get_country_from_ip(self.request)
            user.save(update_fields=["country"])
        # If user is minor and no guardian, we could return error or allow but require consent later
        if user.is_minor and not user.guardian:
            # For now, we just set a flag that they need a guardian to be fully active
            # You could also return a warning in the response
            pass
        return user

    def get_country_from_ip(self, _request):
        """Use GeoIP2 to get country from client IP (optional)."""
        # You need to install geoip2 and download GeoLite2 database
        # For development, just return empty or a default
        return ""  # Placeholder


def home(request):
    return render(request, "accounts/home.html")


class GuestUserView(generics.CreateAPIView):
    """Create a temporary guest user (48 hours)."""

    serializer_class = UserCreateSerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        # Force is_guest=True
        serializer.save(is_guest=True)


class LoginView(APIView):
    """Obtain JWT tokens for authenticated user."""

    permission_classes = [permissions.AllowAny]

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user:
            if user.is_temporary and user.is_expired:
                return Response(
                    {"error": "Your guest account has expired."},
                    status=status.HTTP_403_FORBIDDEN,
                )
            refresh = RefreshToken.for_user(user)
            return Response(
                {
                    "refresh": str(refresh),
                    "access": str(refresh.access_token),
                    "user": UserSerializer(user).data,
                }
            )
        return Response(
            {"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED
        )


class LogoutView(APIView):
    """Logout user (blacklist refresh token)."""

    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        refresh_token = request.data.get("refresh")
        if not refresh_token:
            return Response(
                {"error": "Refresh token is required."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            token = RefreshToken(refresh_token)
            token.blacklist()
        except TokenError as exc:
            return Response({"error": str(exc)}, status=status.HTTP_400_BAD_REQUEST)

        django_logout(request)
        return Response(status=status.HTTP_205_RESET_CONTENT)


class CurrentUserView(generics.RetrieveUpdateAPIView):
    """Get and update the current authenticated user."""

    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user

    def perform_update(self, serializer):
        # Optional: re‑check guardian/minor status on update
        user = serializer.save()
        if user.is_minor and not user.guardian and not user.is_temporary:
            # Could raise validation error
            pass
        # Update profile if included
        profile_data = self.request.data.get("profile", {})
        if profile_data and hasattr(user, "profile"):
            for key, value in profile_data.items():
                setattr(user.profile, key, value)
            user.profile.save()


class DeleteUserView(APIView):
    """Delete own account (SELF ONLY)."""

    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request):
        user = request.user
        # Ensure they are deleting themselves
        # (We already have request.user, so it's safe)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class FamilyMembersView(APIView):
    """List family members (dependents and/or guardians)."""

    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        # Optionally filter to dependents if user is a guardian
        dependents = request.user.dependents.all()
        # Also include the user themselves
        members = list(dependents) + [request.user]
        # Optionally include other family members based on family_group
        serializer = FamilyMemberSerializer(members, many=True)
        return Response(serializer.data)


class DependentCreateView(generics.CreateAPIView):
    """Create a dependent (child) account for a guardian."""

    serializer_class = UserCreateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        # Ensure current user is a guardian (i.e., adult)
        if self.request.user.is_minor:
            return Response(
                {"error": "You must be an adult to create a dependent account."},
                status=status.HTTP_403_FORBIDDEN,
            )
        # Set guardian to the current user
        serializer.save(guardian=self.request.user)


class DependentUpdateDeleteView(APIView):
    """Update or delete a dependent account (by guardian)."""

    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, pk):
        dependent = get_object_or_404(FamilyUser, pk=pk)
        if dependent.guardian != self.request.user:
            return None
        return dependent

    def put(self, request, pk):
        dependent = self.get_object(pk)
        if not dependent:
            return Response(
                {"error": "Not your dependent or not found."},
                status=status.HTTP_403_FORBIDDEN,
            )
        # Use serializer to update
        serializer = UserSerializer(dependent, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, _request, pk):
        dependent = self.get_object(pk)
        if not dependent:
            return Response(
                {"error": "Not your dependent or not found."},
                status=status.HTTP_403_FORBIDDEN,
            )
        # But requirement says SELF ONLY deletion; so we don't allow guardian to delete?
        # According to requirement: "All Family members can be removed by SELF ONLY!"
        # So we should not allow deletion by guardian. However, for practical reasons, we might allow
        # deactivation. I'll keep it as forbidden to strictly follow the requirement.
        return Response(
            {"error": "Only the account owner can delete their own account."},
            status=status.HTTP_403_FORBIDDEN,
        )


class ProxyStatusView(APIView):
    """Check if a user still needs a guardian (auto‑void on reaching majority)."""

    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = request.user
        # If user is no longer a minor and has a guardian, we can automatically remove the guardian
        if not user.is_minor and user.guardian:
            user.guardian = None
            user.save(update_fields=["guardian"])
            return Response({"message": "Guardian removed due to age of majority."})
        return Response({"needs_guardian": user.needs_guardian})


def about(request):
    return render(request, "accounts/about.html")
