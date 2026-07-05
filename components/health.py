import streamlit as st


def city_health_score(reports, critical):

    if reports == 0:

        score = 100

    else:

        score = max(
            0,
            100 - ((critical / reports) * 100)
        )

    if score >= 90:

        colour = "🟢"

    elif score >= 70:

        colour = "🟡"

    else:

        colour = "🔴"

    st.metric(

        "City Health",

        f"{score:.0f}%",

        delta=f"{colour}"

    )

    return score