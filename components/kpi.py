import streamlit as st


def show_kpis(df):

    st.subheader("📈 Operational KPIs")

    total = len(df)

    critical = len(df[df["Priority"] == "Critical"])

    infrastructure = len(
        df[df["Category"] == "Infrastructure"]
    )

    utilities = len(
        df[df["Category"] == "Utilities"]
    )

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Reports", total)

    c2.metric("Critical", critical)

    c3.metric("Infrastructure", infrastructure)

    c4.metric("Utilities", utilities)