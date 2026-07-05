import streamlit as st

# ==========================================================
# PAGE CONFIGURATION (must be the first Streamlit command)
# ==========================================================

st.set_page_config(
    page_title="CORTEX AI Command Center",
    page_icon="🏙",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================================
# INITIALIZE DATABASE
# ==========================================================

from database.database import initialize

initialize()

# ==========================================================
# DASHBOARD PAGES
# ==========================================================

from dashboard.home import show_dashboard
from dashboard.upload import upload_page
from dashboard.analytics import analytics_page
from dashboard.incidents import incidents_page
from dashboard.settings import settings_page

# ==========================================================
# COMPONENTS
# ==========================================================

from components.sidebar import sidebar

# ==========================================================
# SIDEBAR
# ==========================================================

page = sidebar()

# ==========================================================
# ROUTING
# ==========================================================

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