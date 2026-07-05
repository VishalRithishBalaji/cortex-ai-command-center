import cv2
import os

def extract_middle_frame(video_path, output_path):

    print("Opening:", video_path)

    if not os.path.exists(video_path):
        raise FileNotFoundError(video_path)

    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        raise RuntimeError("OpenCV could not open the video.")

    total = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    print("Total Frames:", total)

    if total == 0:
        raise RuntimeError("Video contains zero frames.")

    middle = total // 2

    cap.set(cv2.CAP_PROP_POS_FRAMES, middle)

    success, frame = cap.read()

    if not success:
        raise RuntimeError("Failed to read middle frame.")

    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    cv2.imwrite(output_path, frame)

    cap.release()

    print("Saved:", output_path)

    return output_path