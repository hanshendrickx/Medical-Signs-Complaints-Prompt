from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid


class FamilyUser(AbstractUser):
    """Extended user model for family members"""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    family_group = models.CharField(max_length=50, blank=True)
    is_family_admin = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=15, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)

    # Medical consent for minors
    medical_consent_given = models.BooleanField(default=False)
    guardian = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="dependents",
    )

    class Meta:
        permissions = [
            ("view_family_data", "Can view family medical data"),
        ]

    def __str__(self):
        return f"{self.username} ({self.get_full_name()})"


class FamilyGroup(models.Model):
    """Group family members together"""

    name = models.CharField(max_length=100)
    created_by = models.ForeignKey(FamilyUser, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    invite_code = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name


class FamilyMemberProfile(models.Model):
    """Detailed profile for each family member"""

    user = models.OneToOneField(
        FamilyUser, on_delete=models.CASCADE, related_name="profile"
    )
    family_group = models.ForeignKey(
        FamilyGroup, on_delete=models.CASCADE, related_name="members"
    )
    is_active = models.BooleanField(default=True)

    # Emergency contact
    emergency_contact_name = models.CharField(max_length=100, blank=True)
    emergency_contact_phone = models.CharField(max_length=15, blank=True)

    # Medical ID info
    blood_type = models.CharField(max_length=5, blank=True)
    allergies = models.TextField(blank=True)
    chronic_conditions = models.TextField(blank=True)
    medications = models.TextField(blank=True)

    def __str__(self):
        return f"Profile: {self.user.get_full_name()}"


# Create your models here.
