from rest_framework import serializers
from .models import ComplaintSession, ReportedSymptom, CurrentComplaint, Symptom


class SymptomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Symptom
        fields = ["id", "name", "category", "common_description", "follow_up_questions"]


class ReportedSymptomSerializer(serializers.ModelSerializer):
    symptom_details = SymptomSerializer(source="symptom", read_only=True)

    class Meta:
        model = ReportedSymptom
        fields = [
            "id",
            "symptom",
            "symptom_details",
            "severity",
            "duration",
            "onset",
            "location",
            "details",
            "follow_up_answers",
            "created_at",
        ]


class CurrentComplaintSerializer(serializers.ModelSerializer):
    class Meta:
        model = CurrentComplaint
        fields = [
            "id",
            "description",
            "started_at",
            "frequency",
            "triggers",
            "created_at",
        ]


class ComplaintSessionSerializer(serializers.ModelSerializer):
    reported_symptoms = ReportedSymptomSerializer(many=True, read_only=True)
    current_complaints = CurrentComplaintSerializer(many=True, read_only=True)
    family_member_name = serializers.CharField(
        source="family_member.get_full_name", read_only=True
    )

    class Meta:
        model = ComplaintSession
        fields = [
            "id",
            "family_member",
            "family_member_name",
            "created_at",
            "is_active",
            "temperature",
            "heart_rate",
            "blood_pressure_systolic",
            "blood_pressure_diastolic",
            "oxygen_saturation",
            "reported_symptoms",
            "current_complaints",
        ]


class SymptomSummarySerializer(serializers.Serializer):
    """Serializer for generating AI-ready summary"""

    def to_representation(self, instance):
        session = instance
        summary = {
            "session_id": str(session.id),
            "family_member": session.family_member.get_full_name(),
            "date": session.created_at.date(),
            "vital_signs": {
                "temperature": session.temperature,
                "heart_rate": session.heart_rate,
                "blood_pressure": (
                    f"{session.blood_pressure_systolic}/{session.blood_pressure_diastolic}"
                    if session.blood_pressure_systolic
                    else None
                ),
                "oxygen_saturation": session.oxygen_saturation,
            },
            "reported_symptoms": [],
            "current_complaints": [],
        }

        for symptom in session.reported_symptoms.all():
            summary["reported_symptoms"].append(
                {
                    "name": symptom.symptom.name,
                    "severity": symptom.get_severity_display(),
                    "duration": symptom.duration,
                    "onset": symptom.onset,
                    "location": symptom.location,
                    "details": symptom.details,
                    "follow_up_answers": symptom.follow_up_answers,
                }
            )

        for complaint in session.current_complaints.all():
            summary["current_complaints"].append(
                {
                    "description": complaint.description,
                    "started": complaint.started_at,
                    "frequency": complaint.frequency,
                    "triggers": complaint.triggers,
                }
            )

        return summary
