from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView
from ..models import MaintenanceType
from maintenance_app.mixins import ManagerMaintenanceGroupTestMixin


class MaintenanceSchemesDetail(
    LoginRequiredMixin, ManagerMaintenanceGroupTestMixin, DetailView
):
    model = MaintenanceType
    template_name = "maintenance/maintenance_schemes_detail.html"
    context_object_name = "scheme"
