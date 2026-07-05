import os
import sqlite3
import streamlit as st

from database.schema import SCHEMA
from config.settings import DB_PATH


@st.cache_resource
def initialize():
    # Ensure the database directory exists
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)

    conn = sqlite3.connect(DB_PATH)

    conn.executescript(SCHEMA)

    conn.commit()

    conn.close()