import sqlite3

from config.settings import DB_PATH


class ReportRepository:

    def __init__(self):

        self.db = DB_PATH

    def connection(self):

        return sqlite3.connect(self.db)

    # ----------------------------------------

    def save_report(self, report):

        conn = self.connection()

        cursor = conn.cursor()

        cursor.execute("""

INSERT INTO reports(

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

VALUES(

?,?,?,?,?,?,?,?,?,?,?,?,?,?

)

""",(

report["incident_type"],

report["category"],

report.get("location","Unknown"),

report.get("latitude",0),

report.get("longitude",0),

report["risk_index"],

report["severity"],

report["priority"],

report["recommended_department"],

report["estimated_repair_cost"],

report["estimated_repair_time_days"],

report["traffic_impact"],

report["environmental_impact"],

report["executive_summary"]

))

        conn.commit()

        conn.close()

    # ----------------------------------------

    def get_reports(self):

        conn=self.connection()

        cursor=conn.cursor()

        cursor.execute("""

SELECT *

FROM reports

ORDER BY created_at DESC

""")

        rows=cursor.fetchall()

        conn.close()

        return rows

    # ----------------------------------------

    def total_reports(self):

        conn=self.connection()

        cursor=conn.cursor()

        cursor.execute("""

SELECT COUNT(*)

FROM reports

""")

        value=cursor.fetchone()[0]

        conn.close()

        return value

    # ----------------------------------------

    def critical_reports(self):

        conn=self.connection()

        cursor=conn.cursor()

        cursor.execute("""

SELECT COUNT(*)

FROM reports

WHERE priority='Critical'

""")

        value=cursor.fetchone()[0]

        conn.close()

        return value

    # ----------------------------------------

    def average_cost(self):

        conn=self.connection()

        cursor=conn.cursor()

        cursor.execute("""

SELECT AVG(estimated_repair_cost)

FROM reports

""")

        value=cursor.fetchone()[0]

        conn.close()

        return value or 0

    # ----------------------------------------

    def maintenance_budget(self):

        conn=self.connection()

        cursor=conn.cursor()

        cursor.execute("""

SELECT SUM(estimated_repair_cost)

FROM reports

WHERE status='Pending'

""")

        value=cursor.fetchone()[0]

        conn.close()

        return value or 0

    # ----------------------------------------

    def incident_frequency(self):

        conn=self.connection()

        cursor=conn.cursor()

        cursor.execute("""

SELECT

incident_type,

COUNT(*)

FROM reports

GROUP BY incident_type

ORDER BY COUNT(*) DESC

""")

        rows=cursor.fetchall()

        conn.close()

        return rows