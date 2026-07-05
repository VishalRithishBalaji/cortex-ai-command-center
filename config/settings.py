from dotenv import load_dotenv
import os

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

PROJECT_NAME = "CORTEX"

CITY = "Coimbatore"

DB_PATH = "database/cortex.db"

VECTOR_DB = "vector_db"

UPLOAD_FOLDER = "data/uploads"

REPORT_FOLDER = "data/reports"