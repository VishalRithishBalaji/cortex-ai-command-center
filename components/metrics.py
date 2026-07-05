import streamlit as st


def city_health_score(reports, critical):

    if reports == 0:
        score = 100

    else:
        score = max(
            0,
            100 - (critical / reports) * 100
        )

    st.metric(
        "🏙 City Health Score",
        f"{score:.0f}%"
    )