"""
CORTEX v2 - Recommendation Engine
---------------------------------
Generates:
1. Priority
2. Recommended Action
3. Department
4. Escalation Level
5. Citizen Alert
"""

RECOMMENDATION_RULES = {
    "Pothole": {
        "department": "Road Maintenance Department",
        "action": "Dispatch emergency road repair team.",
        "citizen_alert": "Drive carefully. Road repair scheduled.",
        "escalation": "Engineering Division"
    },

    "Broken Footpath": {
        "department": "Civil Engineering Department",
        "action": "Repair damaged footpath immediately.",
        "citizen_alert": "Pedestrians should avoid this pathway.",
        "escalation": "Infrastructure Division"
    },

    "Garbage Dump": {
        "department": "Sanitation Department",
        "action": "Schedule garbage collection within 24 hours.",
        "citizen_alert": "Waste removal team has been notified.",
        "escalation": "Public Health Division"
    },

    "Water Leakage": {
        "department": "Water Supply Board",
        "action": "Dispatch maintenance crew to stop leakage.",
        "citizen_alert": "Avoid flooded area.",
        "escalation": "Utilities Division"
    },

    "Street Light Failure": {
        "department": "Electrical Department",
        "action": "Replace faulty street light.",
        "citizen_alert": "Area has reduced visibility during night.",
        "escalation": "Electrical Division"
    }
}


def generate(report):
    """
    Enrich AI report with operational recommendations.
    """

    # No incident detected
    if report["incident_type"] == "Normal Operations":

        report["priority"] = "None"

        report["recommended_department"] = "None"

        report["recommended_action"] = "No Action Required"

        report["citizen_alert"] = "No public advisory required."

        report["escalation_level"] = "None"

        return report

    # Existing logic continues here...

    risk = report.get("risk_index", report.get("severity", 0))
    incident = report.get("incident_type", "Unknown")

    # -------------------------
    # Priority
    # -------------------------
    if risk >= 80:
        priority = "Critical"

    elif risk >= 60:
        priority = "High"

    elif risk >= 40:
        priority = "Medium"

    else:
        priority = "Low"

    report["priority"] = priority

    # -------------------------
    # Recommendation Rules
    # -------------------------
    rule = RECOMMENDATION_RULES.get(
        incident,
        {
            "department": "Municipal Operations",
            "action": "Manual inspection required.",
            "citizen_alert": "Authorities have been notified.",
            "escalation": "Operations Center"
        }
    )

    report["recommended_department"] = rule["department"]
    report["recommended_action"] = rule["action"]
    report["citizen_alert"] = rule["citizen_alert"]
    report["escalation_level"] = rule["escalation"]

    return report