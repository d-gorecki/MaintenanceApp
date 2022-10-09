from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from ..models import MalfunctionReport
from maintenance_app.mixins import ManagerMaintenanceGroupTestMixin


class MalfunctionsReports(
    LoginRequiredMixin, ManagerMaintenanceGroupTestMixin, ListView
):
    model = MalfunctionReport
    template_name = "malfunctions/malfunctions_reports.html"
    ordering = ["-id"]
    context_object_name = "malfunction_reports"
