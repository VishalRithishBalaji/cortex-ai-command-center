import streamlit as st

from repository.report_repository import ReportRepository

repo = ReportRepository()


def incidents_page():

    st.title("🚨 Incident History")

    rows = repo.get_reports()

    if rows:

        st.dataframe(
            rows,
            use_container_width=True,
            hide_index=True
        )

    else:

        st.info("No incidents available.")