from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from malfunctions.models.malfunction_report import MalfunctionReport
from maintenance_app.mixins import ManagerMaintenanceGroupTestMixin


class MalfunctionsReports(
    LoginRequiredMixin, ManagerMaintenanceGroupTestMixin, ListView
):
    """Base view for malfunctions reports (sub-module of malfunctions app)"""

    model: MalfunctionReport = MalfunctionReport
    template_name: str = "malfunctions/malfunctions_reports.html"
    ordering: list[str] = ["-id"]
    context_object_name: str = "malfunction_reports"
