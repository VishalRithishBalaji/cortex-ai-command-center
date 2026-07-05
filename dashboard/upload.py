import streamlit as st
import os

from services.upload_service import UploadService


service = UploadService()


def upload_page():

    st.header("Upload Incident")

    uploaded = st.file_uploader(

        "Upload Video",

        type=["mp4"]

    )

    if uploaded:

        save_path = os.path.join(

            "data/uploads",

            uploaded.name

        )

        with open(save_path, "wb") as f:

            f.write(uploaded.read())

        if st.button("Analyze"):

            with st.spinner("Running CORTEX..."):

                report = service.process_video(save_path)

            st.success("Analysis Completed")

            st.json(report)