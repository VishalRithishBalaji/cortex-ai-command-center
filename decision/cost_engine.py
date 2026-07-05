def estimate(report):

    incident = report["incident_type"]

    TABLE = {

        "Pothole":5000,

        "Garbage Dump":3000,

        "Water Leakage":8000,

        "Broken Footpath":12000,

        "Street Light Failure":2500

    }

    report["estimated_repair_cost"] = TABLE.get(

        incident,

        report["estimated_repair_cost"]

    )

    return report