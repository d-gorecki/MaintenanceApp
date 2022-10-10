from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView
from ..models import MaintenanceReport
from maintenance_app.mixins import ManagerMaintenanceGroupTestMixin


class MaintenanceReportsDetail(
    LoginRequiredMixin, ManagerMaintenanceGroupTestMixin, DetailView
):
    """Detail view for maintenance reports (sub-module of maintenance app)"""

    model: MaintenanceReport = MaintenanceReport
    template_name: str = "maintenance/maintenance_reports_detail.html"
