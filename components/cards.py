import streamlit as st

from components.health import city_health_score


def show_cards(data):

    reports = data["reports"]

    critical = data["critical"]

    budget = data["maintenance_budget"]

    average = data["average_cost"]

    c1, c2, c3, c4 = st.columns(4)

    with c1:

        score = city_health_score(

            reports,

            critical

        )

    with c2:

        st.metric(

            "Reports",

            reports

        )

    with c3:

        st.metric(

            "Critical",

            critical

        )

    with c4:

        st.metric(

            "Budget",

            f"₹ {budget:,.0f}"

        )

    st.metric(

        "Average Repair Cost",

        f"₹ {average:,.0f}"

    )

    return score