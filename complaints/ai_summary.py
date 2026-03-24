"""
Module for generating AI-ready summaries of medical complaints
"""


def generate_ai_prompt(session):
    """
    Generate a structured prompt for AI based on the complaint session

    Returns a formatted text ready to be sent to an AI
    """

    family_member = session.family_member
    symptoms = session.reported_symptoms.all()
    complaints = session.current_complaints.all()

    # Build the medical summary
    summary_parts = []

    # Header
    summary_parts.append(f"MEDICAL SUMMARY FOR: {family_member.get_full_name()}")
    summary_parts.append(f"Date: {session.created_at.strftime('%Y-%m-%d %H:%M')}")
    summary_parts.append("")

    # Vital signs if available
    if any([session.temperature, session.heart_rate, session.blood_pressure_systolic]):
        summary_parts.append("VITAL SIGNS:")
        if session.temperature:
            summary_parts.append(f"- Temperature: {session.temperature}°C")
        if session.heart_rate:
            summary_parts.append(f"- Heart Rate: {session.heart_rate} bpm")
        if session.blood_pressure_systolic:
            summary_parts.append(
                f"- Blood Pressure: {session.blood_pressure_systolic}/{session.blood_pressure_diastolic}"
            )
        if session.oxygen_saturation:
            summary_parts.append(f"- O2 Saturation: {session.oxygen_saturation}%")
        summary_parts.append("")

    # Reported symptoms
    if symptoms:
        summary_parts.append("REPORTED SYMPTOMS:")
        for symptom in symptoms:
            summary_parts.append(f"\n• {symptom.symptom.name}:")
            summary_parts.append(f"  - Severity: {symptom.get_severity_display()}")
            summary_parts.append(f"  - Duration: {symptom.duration}")
            summary_parts.append(f"  - Onset: {symptom.onset}")
            if symptom.location:
                summary_parts.append(f"  - Location: {symptom.location}")
            if symptom.details:
                for key, value in symptom.details.items():
                    summary_parts.append(f"  - {key}: {value}")
            if symptom.follow_up_answers:
                summary_parts.append("  - Additional Details:")
                for q, a in symptom.follow_up_answers.items():
                    summary_parts.append(f"    * {q}: {a}")

    # Current complaints
    if complaints:
        summary_parts.append("\nCURRENT COMPLAINTS:")
        for complaint in complaints:
            summary_parts.append(f"\n• {complaint.description}")
            summary_parts.append(f"  - Started: {complaint.started_at}")
            if complaint.frequency:
                summary_parts.append(f"  - Frequency: {complaint.frequency}")
            if complaint.triggers:
                summary_parts.append(f"  - Triggers/Relievers: {complaint.triggers}")

    # Create the AI prompt
    prompt = f"""
You are a medical AI assistant. Based on the following medical summary, please answer these questions:

1. Do I Need A Doctor? (Assess urgency and provide recommendation)
2. Trustworthy Guidelines for patients (Patient-friendly advice and self-care)
3. Guidelines for Physicians (Clinical perspective and considerations)
4. Questions an experienced physician would ask me (Follow-up questions for better diagnosis)

MEDICAL SUMMARY:
{chr(10).join(summary_parts)}

Please provide clear, organized answers to all four questions. Include appropriate disclaimers that this is not a substitute for professional medical advice.
"""

    return prompt


def format_for_ai_api(session, api_type="openai"):
    """
    Format the summary for specific AI APIs
    """
    base_prompt = generate_ai_prompt(session)

    if api_type == "openai":
        return {
            "model": "gpt-4",
            "messages": [
                {
                    "role": "system",
                    "content": "You are a helpful medical assistant providing preliminary guidance.",
                },
                {"role": "user", "content": base_prompt},
            ],
            "temperature": 0.7,
            "max_tokens": 1000,
        }
    elif api_type == "claude":
        return {
            "prompt": f"\n\nHuman: {base_prompt}\n\nAssistant: I'll provide a medical analysis based on this information:",
            "max_tokens_to_sample": 1000,
        }

    return base_prompt
