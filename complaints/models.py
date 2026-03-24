from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
import uuid


class SymptomCategory(models.Model):
    """Categories of symptoms (e.g., Pain, Fever, etc.)"""

    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = "Symptom Categories"

    def __str__(self):
        return self.name


class Symptom(models.Model):
    """Predefined symptoms that can be selected"""

    name = models.CharField(max_length=200)
    category = models.ForeignKey(
        SymptomCategory, on_delete=models.CASCADE, related_name="symptoms"
    )
    common_description = models.TextField(blank=True)
    follow_up_questions = models.JSONField(
        default=list
    )  # Store questions to ask about this symptom

    def __str__(self):
        return self.name


class ComplaintSession(models.Model):
    """A session of complaint collection for a family member"""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="complaint_sessions",
    )
    family_member = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="medical_sessions",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    # Vital signs
    temperature = models.FloatField(null=True, blank=True)
    heart_rate = models.IntegerField(null=True, blank=True)
    blood_pressure_systolic = models.IntegerField(null=True, blank=True)
    blood_pressure_diastolic = models.IntegerField(null=True, blank=True)
    oxygen_saturation = models.IntegerField(
        null=True, blank=True, validators=[MinValueValidator(0), MaxValueValidator(100)]
    )

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"Session for {self.family_member.username} - {self.created_at.date()}"


class ReportedSymptom(models.Model):
    """Individual symptom reported in a session"""

    SEVERITY_CHOICES = [
        (1, "Mild"),
        (2, "Moderate"),
        (3, "Severe"),
        (4, "Very Severe"),
        (5, "Emergency"),
    ]

    session = models.ForeignKey(
        ComplaintSession, on_delete=models.CASCADE, related_name="reported_symptoms"
    )
    symptom = models.ForeignKey(Symptom, on_delete=models.CASCADE)

    # Details
    severity = models.IntegerField(choices=SEVERITY_CHOICES)
    duration = models.CharField(max_length=100)  # e.g., "2 days", "1 week"
    onset = models.CharField(max_length=100)  # e.g., "sudden", "gradual"
    location = models.CharField(max_length=200, blank=True)  # For pain location

    # Additional details stored as JSON for flexibility
    details = models.JSONField(default=dict)

    # Follow-up answers
    follow_up_answers = models.JSONField(default=dict)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.symptom.name} - Severity: {self.severity}"


class CurrentComplaint(models.Model):
    """Current complaints that don't fit into symptoms"""

    session = models.ForeignKey(
        ComplaintSession, on_delete=models.CASCADE, related_name="current_complaints"
    )
    description = models.TextField()
    started_at = models.CharField(max_length=100)  # When it started
    frequency = models.CharField(
        max_length=100, blank=True
    )  # Constant, intermittent, etc.
    triggers = models.TextField(blank=True)  # What makes it better/worse

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Complaint: {self.description[:50]}..."


# Create your models here.
