import streamlit as st


def ask_cortex(df):

    st.subheader("🤖 Ask CORTEX")

    question = st.text_input(
        "Ask a question about city operations"
    )

    if not question:

        return

    q = question.lower()

    if "critical" in q:

        value = len(df[df["Priority"] == "Critical"])

        st.info(
            f"There are {value} critical incidents."
        )

    elif "budget" in q:

        budget = df["Repair Cost"].sum()

        st.info(
            f"Estimated maintenance budget is ₹{budget:,.0f}"
        )

    elif "department" in q:

        top = (
            df["Department"]
            .value_counts()
            .idxmax()
        )

        st.info(
            f"The busiest department is {top}."
        )

    else:

        st.warning(
            "Question not supported yet. Gemini chat arrives in Phase 5."
        )