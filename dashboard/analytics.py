import streamlit as st

from services.analytics_service import dashboard


def analytics_page():

    st.header("📊 Analytics")

    data = dashboard()

    st.json(data)