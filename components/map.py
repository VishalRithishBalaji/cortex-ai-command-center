import streamlit as st
import pandas as pd


def show_map(df):

    st.subheader("📍 Live Incident Map")

    if df.empty:

        st.info("No location data available.")

        return

    if "Latitude" not in df.columns:

        return

    map_df = pd.DataFrame({
        "lat": df["Latitude"],
        "lon": df["Longitude"]
    })

    st.map(map_df)