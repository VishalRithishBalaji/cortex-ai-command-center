import plotly.express as px


def incident_chart(df):

    fig = px.pie(
        df,
        names="Incident",
        title="Incident Distribution"
    )

    return fig


def department_chart(df):

    fig = px.bar(
        df,
        x="Department",
        title="Department Workload"
    )

    return fig