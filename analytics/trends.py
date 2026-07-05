from repository.report_repository import ReportRepository

repo = ReportRepository()


def incident_frequency():

    return repo.incident_frequency()