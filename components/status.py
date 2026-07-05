import streamlit as st


def operational_status(score):

    if score >= 90:

        status = "🟢 OPERATIONAL"

    elif score >= 70:

        status = "🟡 WARNING"

    else:

        status = "🔴 CRITICAL"

    st.subheader("Operational Status")

    st.success(status)