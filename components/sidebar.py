from streamlit_option_menu import option_menu
import streamlit as st


def sidebar():

    with st.sidebar:

        st.image(
            "https://img.icons8.com/fluency/96/city-buildings.png",
            width=70
        )

        st.markdown("## CORTEX")

        st.caption("AI Decision Intelligence Platform")

        selected = option_menu(
            menu_title=None,

            options=[
                "Dashboard",
                "Upload",
                "Analytics",
                "Incidents",
                "Settings"
            ],

            icons=[
                "speedometer2",
                "cloud-upload",
                "bar-chart",
                "exclamation-triangle",
                "gear"
            ],

            default_index=0,

            styles={
                "container": {
                    "padding": "5px"
                },
                "icon": {
                    "color": "#00C853",
                    "font-size": "18px"
                },
                "nav-link": {
                    "font-size": "16px",
                    "text-align": "left",
                    "margin": "4px",
                    "--hover-color": "#1E1E1E"
                },
                "nav-link-selected": {
                    "background-color": "#00C853"
                },
            }
        )

    return selected