import uuid
from datetime import timedelta
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError


class FamilyUser(AbstractUser):
    """Extended user model with family, guest, and proxy features."""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    family_group = models.CharField(
        max_length=50, blank=True, help_text="Family name (optional)"
    )
    is_family_admin = models.BooleanField(
        default=False, help_text="Can manage other family members"
    )
    phone_number = models.CharField(max_length=15, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    medical_consent_given = models.BooleanField(
        default=False, help_text="For minors: parental consent"
    )

    # Guardian relation for minors
    guardian = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="dependents",
        help_text="Parent/guardian of this user (if minor)",
    )

    # Guest / temporary accounts
    is_temporary = models.BooleanField(
        default=False, help_text="Guest account with expiry"
    )
    expires_at = models.DateTimeField(
        null=True, blank=True, help_text="When this temporary account expires"
    )

    # Location for international rules
    country = models.CharField(
        max_length=2, blank=True, help_text="ISO country code (e.g., US, DE)"
    )

    class Meta:
        permissions = [
            ("view_family_data", "Can view medical data of family members"),
            ("manage_children", "Can create and manage child accounts"),
        ]

    def __str__(self):
        return f"{self.username} ({self.get_full_name()})"

    @property
    def is_expired(self):
        """Return True if this is a temporary user and the expiry date has passed."""
        if not self.is_temporary or not self.expires_at:
            return False
        return self.expires_at <= timezone.now()

    @property
    def age(self):
        """Calculate age from date_of_birth (if available)."""
        if not self.date_of_birth:
            return None
        today = timezone.now().date()
        return (
            today.year
            - self.date_of_birth.year
            - (
                (today.month, today.day)
                < (self.date_of_birth.month, self.date_of_birth.day)
            )
        )

    @property
    def age_of_majority(self):
        """Return the legal adult age based on country (default 18)."""
        # You can extend this with a country-to-age mapping
        ages = {
            "US": 18,
            "CA": 18,
            "GB": 18,
            "DE": 18,
            "FR": 18,
            "JP": 20,
            # Add more as needed
        }
        return ages.get(self.country, 18)

    @property
    def is_minor(self):
        """Return True if the user is under the age of majority."""
        if self.age is None:
            # If DOB not set, assume adult (or maybe require DOB)
            return False
        return self.age < self.age_of_majority

    @property
    def needs_guardian(self):
        """Return True if the user is a minor and has no guardian set."""
        return self.is_minor and self.guardian is None

    def clean(self):
        """Validate model constraints."""
        if self.is_temporary and self.expires_at is None:
            raise ValidationError("Temporary users must have an expiry date.")
        if self.is_minor and not self.guardian and not self.is_temporary:
            # For permanent minor accounts, require a guardian
            raise ValidationError("Minors must have a guardian assigned.")

    def save(self, *args, **kwargs):
        # Auto‑set expiry for temporary accounts if not set
        if self.is_temporary and not self.expires_at:
            self.expires_at = timezone.now() + timedelta(hours=48)
        self.full_clean()  # Run validation
        super().save(*args, **kwargs)

    def can_be_managed_by(self, user):
        """Check if the given user can manage this account (e.g., as guardian)."""
        if self == user:
            return True
        if self.guardian == user:
            return True
        if user.is_superuser:
            return True
        return False


class FamilyGroup(models.Model):
    """Optional grouping of family members (for multi‑family setups)."""

    name = models.CharField(max_length=100)
    created_by = models.ForeignKey(FamilyUser, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    invite_code = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name


class FamilyMemberProfile(models.Model):
    """Detailed profile for each family member."""

    user = models.OneToOneField(
        FamilyUser, on_delete=models.CASCADE, related_name="profile"
    )
    family_group = models.ForeignKey(
        FamilyGroup,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="members",
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
