from repository.report_repository import ReportRepository

repo = ReportRepository()


def total_reports():

    return repo.total_reports()


def critical():

    return repo.critical_reports()


def average_cost():

    return repo.average_cost()