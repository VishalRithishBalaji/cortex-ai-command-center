import os
import sqlite3
import streamlit as st

from database.schema import SCHEMA
from config.settings import (
    DB_PATH,
    UPLOAD_FOLDER,
    REPORT_FOLDER
)


@st.cache_resource
def initialize():
    # -----------------------------------------
    # Create required folders
    # -----------------------------------------

    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    os.makedirs("data/processed", exist_ok=True)
    os.makedirs(REPORT_FOLDER, exist_ok=True)

    # -----------------------------------------
    # Create database
    # -----------------------------------------

    conn = sqlite3.connect(DB_PATH)

    conn.executescript(SCHEMA)

    conn.commit()

    conn.close()