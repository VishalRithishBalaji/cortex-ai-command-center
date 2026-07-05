import os

from preprocessing.frame_selector import get_best_frame

from ai.gemini import analyze

from services.decision_service import DecisionService

from repository.report_repository import ReportRepository


class UploadService:

    def __init__(self):

        self.repo = ReportRepository()

        self.decision = DecisionService()

    # --------------------------------------------------

    def process_video(self, video_path):

        frame = get_best_frame(video_path)

        report = analyze(frame)

        report = self.decision.process(report)

        self.repo.save_report(report)

        return report