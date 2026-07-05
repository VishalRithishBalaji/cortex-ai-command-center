SCHEMA = """

CREATE TABLE IF NOT EXISTS reports(

id INTEGER PRIMARY KEY AUTOINCREMENT,

incident_type TEXT,

category TEXT,

location TEXT,

latitude REAL,

longitude REAL,

risk_index INTEGER,

severity INTEGER,

priority TEXT,

recommended_department TEXT,

estimated_repair_cost INTEGER,

estimated_repair_time_days INTEGER,

traffic_impact TEXT,

environmental_impact TEXT,

executive_summary TEXT,

status TEXT DEFAULT 'Pending',

created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

);

"""