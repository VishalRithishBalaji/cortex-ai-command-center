from repository.report_repository import ReportRepository

repo = ReportRepository()


def dashboard():

    return {

        "reports": repo.total_reports(),

        "critical": repo.critical_reports(),

        "average_cost": repo.average_cost(),

        "maintenance_budget": repo.maintenance_budget(),

        "trends": repo.incident_frequency()

    }