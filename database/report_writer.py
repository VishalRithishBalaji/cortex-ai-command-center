from repository.report_repository import ReportRepository

repo = ReportRepository()


def save(report):

    repo.save_report(report)