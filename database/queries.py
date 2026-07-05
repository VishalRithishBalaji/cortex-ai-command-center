from repository.report_repository import ReportRepository

repo = ReportRepository()


def get_all_reports():

    return repo.get_reports()