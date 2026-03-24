from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import ComplaintSession, Symptom
from .serializers import (
    ComplaintSessionSerializer,
    SymptomSerializer,
    SymptomSummarySerializer,
)
from .ai_summary import generate_ai_prompt, format_for_ai_api


class SymptomViewSet(viewsets.ReadOnlyModelViewSet):
    """View symptoms that can be reported"""

    queryset = Symptom.objects.all()
    serializer_class = SymptomSerializer
    permission_classes = [IsAuthenticated]


class ComplaintSessionViewSet(viewsets.ModelViewSet):
    """Manage complaint sessions"""

    serializer_class = ComplaintSessionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Users can only see their family's sessions
        user = self.request.user
        if user.is_family_admin:
            # Family admin can see all family members
            return ComplaintSession.objects.filter(
                family_member__profile__family_group__members__user=user
            ).distinct()
        # Regular users can only see their own sessions
        return ComplaintSession.objects.filter(family_member=user)

    def perform_create(self, serializer):
        # Set the creating user
        serializer.save(user=self.request.user)

    @action(detail=True, methods=["get"])
    def summary(self, request, pk=None):
        """Get a summary of the complaint session"""
        session = self.get_object()
        serializer = SymptomSummarySerializer(session)
        return Response(serializer.data)

    @action(detail=True, methods=["get"])
    def ai_prompt(self, request, pk=None):
        """Generate AI-ready prompt"""
        session = self.get_object()
        api_type = request.query_params.get("api", "text")

        if api_type == "text":
            prompt = generate_ai_prompt(session)
            return Response({"prompt": prompt})
        else:
            prompt_data = format_for_ai_api(session, api_type)
            return Response(prompt_data)

    @action(detail=True, methods=["post"])
    def add_symptom(self, request, pk=None):
        """Add a symptom to the session"""
        _session = self.get_object()
        # Logic to add symptom
        return Response({"status": "symptom added"})

    @action(detail=True, methods=["post"])
    def add_complaint(self, request, pk=None):
        """Add a current complaint to the session"""
        _session = self.get_object()
        # Logic to add complaint
        return Response({"status": "complaint added"})


# Create your views here.
