from preprocessing.video import extract_middle_frame

def get_best_frame(upload_path):

    if upload_path.endswith(".mp4"):

        return extract_middle_frame(
            upload_path,
            "data/processed/best_frame.jpg"
        )

    return upload_path