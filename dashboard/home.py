import streamlit as st
import pandas as pd

from services.analytics_service import dashboard
from repository.report_repository import ReportRepository

# Components
from components.header import show_header
from components.cards import show_cards
from components.status import operational_status

from components.kpi import show_kpis
from components.map import show_map
from components.summary import executive_summary
from components.chatbot import ask_cortex

from components.charts import (
    incident_chart,
    department_chart
)

repo = ReportRepository()


def show_dashboard():

    # =====================================================
    # HEADER
    # =====================================================

    show_header()

    analytics = dashboard()

    # =====================================================
    # CITY HEALTH + KPI CARDS
    # =====================================================

    score = show_cards(analytics)

    operational_status(score)

    st.divider()

    # =====================================================
    # LOAD REPORTS
    # =====================================================

    rows = repo.get_reports()

    if not rows:
        st.info("📭 No reports available.")
        return

    columns = [
        "ID",
        "Incident",
        "Category",
        "Location",
        "Latitude",
        "Longitude",
        "Risk Index",
        "Severity",
        "Priority",
        "Department",
        "Repair Cost",
        "Repair Days",
        "Traffic",
        "Environment",
        "Summary",
        "Status",
        "Created At"
    ]

    df = pd.DataFrame(rows, columns=columns)

    # =====================================================
    # OPERATIONAL KPIs
    # =====================================================

    show_kpis(df)

    st.divider()

    # =====================================================
    # LIVE INCIDENT MAP
    # =====================================================

    show_map(df)

    st.divider()

    # =====================================================
    # ANALYTICS CHARTS
    # =====================================================

    st.subheader("📊 Decision Analytics")

    left, right = st.columns(2)

    with left:
        st.plotly_chart(
            incident_chart(df),
            use_container_width=True
        )

    with right:
        st.plotly_chart(
            department_chart(df),
            use_container_width=True
        )

    st.divider()

    # =====================================================
    # EXECUTIVE SUMMARY
    # =====================================================

    executive_summary(df)

    st.divider()

    # =====================================================
    # ASK CORTEX
    # =====================================================

    ask_cortex(df)

    st.divider()

    # =====================================================
    # INCIDENT DATABASE
    # =====================================================

    st.subheader("📋 Incident Database")

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )