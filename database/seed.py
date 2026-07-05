import sqlite3
from config.settings import DB_PATH

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

cursor.execute("""
INSERT INTO reports (
    incident_type,
    category,
    location,
    latitude,
    longitude,
    risk_index,
    severity,
    priority,
    recommended_department,
    estimated_repair_cost,
    estimated_repair_time_days,
    traffic_impact,
    environmental_impact,
    executive_summary
)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
""", (
    "Pothole",
    "Infrastructure",
    "Coimbatore",
    11.0168,
    76.9558,
    85,
    9,
    "Critical",
    "Road Maintenance Department",
    5000,
    2,
    "High",
    "Low",
    "Large pothole detected on a major road."
))

conn.commit()
conn.close()

print("Database Seeded")