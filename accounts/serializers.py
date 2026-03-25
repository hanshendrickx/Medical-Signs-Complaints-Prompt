from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from .models import FamilyUser, FamilyMemberProfile


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = FamilyUser
        fields = (
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
            "phone_number",
            "date_of_birth",
            "country",
            "is_family_admin",
            "is_temporary",
            "expires_at",
            "guardian",
        )
        read_only_fields = ("id", "is_temporary", "expires_at")

    def validate(self, data):
        # If creating a new user and it's not a guest, check guardian for minors
        if self.instance is None:  # creation
            if not data.get("is_temporary", False):
                # For permanent users, if they are minors, a guardian must be provided
                # But guardian may not be in data if it's a self‑signup – we'll handle in view
                pass
        return data


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password]
    )
    is_guest = serializers.BooleanField(write_only=True, default=False)

    class Meta:
        model = FamilyUser
        fields = (
            "username",
            "email",
            "password",
            "first_name",
            "last_name",
            "phone_number",
            "date_of_birth",
            "country",
            "is_guest",
            "guardian",
        )

    def create(self, validated_data):
        is_guest = validated_data.pop("is_guest", False)
        password = validated_data.pop("password")
        user = FamilyUser(**validated_data)
        user.set_password(password)
        user.is_temporary = is_guest
        # If guest, expiry will be set in model save()
        user.save()
        # Create profile (you may want to add more fields)
        FamilyMemberProfile.objects.create(user=user)
        return user


class UserProfileSerializer(serializers.ModelSerializer):
    profile = serializers.SerializerMethodField()

    class Meta:
        model = FamilyUser
        fields = (
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
            "phone_number",
            "date_of_birth",
            "country",
            "is_family_admin",
            "is_temporary",
            "expires_at",
            "guardian",
            "profile",
        )

    def get_profile(self, obj):
        if hasattr(obj, "profile"):
            return {
                "emergency_contact_name": obj.profile.emergency_contact_name,
                "emergency_contact_phone": obj.profile.emergency_contact_phone,
                "blood_type": obj.profile.blood_type,
                "allergies": obj.profile.allergies,
                "chronic_conditions": obj.profile.chronic_conditions,
                "medications": obj.profile.medications,
            }
        return {}


class FamilyMemberSerializer(serializers.ModelSerializer):
    """Simplified view for family members (for listing dependents)."""

    class Meta:
        model = FamilyUser
        fields = (
            "id",
            "username",
            "first_name",
            "last_name",
            "date_of_birth",
            "country",
        )
