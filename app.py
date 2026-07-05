import streamlit as st

# -------------------------------
# Dashboard Pages
# -------------------------------
from dashboard.home import show_dashboard
from dashboard.upload import upload_page
from dashboard.analytics import analytics_page
from dashboard.incidents import incidents_page
from dashboard.settings import settings_page

# -------------------------------
# Components
# -------------------------------
from components.sidebar import sidebar

# -------------------------------
# Page Configuration
# -------------------------------
st.set_page_config(
    page_title="CORTEX AI Command Center",
    page_icon="🏙",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -------------------------------
# Sidebar Navigation
# -------------------------------
page = sidebar()

# -------------------------------
# Route Pages
# -------------------------------
if page == "Dashboard":
    show_dashboard()

elif page == "Upload":
    upload_page()

elif page == "Analytics":
    analytics_page()

elif page == "Incidents":
    incidents_page()

elif page == "Settings":
    settings_page()