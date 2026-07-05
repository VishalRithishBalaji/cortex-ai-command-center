import os
import streamlit as st

from services.upload_service import UploadService
from config.settings import UPLOAD_FOLDER

service = UploadService()


def upload_page():

    st.header("📤 Upload Incident")

    uploaded = st.file_uploader(
        "Upload Video",
        type=["mp4"]
    )

    if uploaded:

        # Ensure upload folder exists
        os.makedirs(UPLOAD_FOLDER, exist_ok=True)

        save_path = os.path.join(
            UPLOAD_FOLDER,
            uploaded.name
        )

        with open(save_path, "wb") as f:
            f.write(uploaded.read())

        st.success(f"Uploaded: {uploaded.name}")

        if st.button("Analyze"):

            with st.spinner("Running CORTEX AI..."):

                report = service.process_video(save_path)

            st.success("Analysis Completed")

            st.json(report)