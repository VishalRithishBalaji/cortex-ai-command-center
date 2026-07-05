# decision/decision_engine.py

CATEGORY_MAP = {

    "Pothole": "Infrastructure",

    "Broken Footpath": "Infrastructure",

    "Street Light Failure": "Utilities",

    "Water Leakage": "Utilities",

    "Garbage Dump": "Waste Management",

    "Illegal Parking": "Traffic",

    "Flooded Road": "Disaster Management",

    "Blocked Sidewalk": "Accessibility",

    "Normal Operations": "Monitoring"

}


def calculate(report):
    """
    Calculate overall risk index and assign category.
    """

    risk = 0

    severity = report.get("severity", 0)
    affected_population = report.get("affected_population", 0)
    traffic = report.get("traffic_impact", "None")
    environment = report.get("environmental_impact", "None")

    # Severity Weight
    risk += severity * 5

    # Population Weight
    risk += affected_population // 10

    # Traffic Weight
    if "High" in traffic:
        risk += 20
    elif "Moderate" in traffic:
        risk += 10

    # Environmental Weight
    if "High" in environment:
        risk += 20
    elif "Moderate" in environment:
        risk += 10

    report["risk_index"] = min(risk, 100)

    # Category Assignment
    report["category"] = CATEGORY_MAP.get(
        report["incident_type"],
        "Other"
    )

    return report