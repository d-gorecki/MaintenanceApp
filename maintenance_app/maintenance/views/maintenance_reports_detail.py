from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView
from ..models import MaintenanceReport
from maintenance_app.mixins import ManagerMaintenanceGroupTestMixin


class MaintenanceReportsDetail(
    LoginRequiredMixin, ManagerMaintenanceGroupTestMixin, DetailView
):
    model = MaintenanceReport
    template_name = "maintenance/maintenance_reports_detail.html"
