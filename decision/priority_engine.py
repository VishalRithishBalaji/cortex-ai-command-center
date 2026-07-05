def calculate_priority(report):

    r = report["risk_index"]

    if r >= 80:
        report["priority"]="Critical"

    elif r>=60:
        report["priority"]="High"

    elif r>=40:
        report["priority"]="Medium"

    else:
        report["priority"]="Low"

    return report