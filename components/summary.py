import streamlit as st


def executive_summary(df):

    st.subheader("🧠 Executive Summary")

    total = len(df)

    if total == 0:

        st.info("No reports available.")

        return

    critical = len(df[df["Priority"] == "Critical"])

    budget = df["Repair Cost"].sum()

    top = (
        df["Incident"]
        .value_counts()
        .idxmax()
    )

    st.success(
        f"""
### Today's Operations

• Reports Processed : **{total}**

• Critical Incidents : **{critical}**

• Estimated Budget : **₹{budget:,.0f}**

• Most Frequent Issue : **{top}**

City operations remain under continuous AI monitoring.
"""
    )