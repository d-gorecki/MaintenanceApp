from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView
from maintenance.models.maintenance_type import MaintenanceType


from maintenance_app.mixins import ManagerMaintenanceGroupTestMixin


class MaintenanceSchemesDetail(
    LoginRequiredMixin, ManagerMaintenanceGroupTestMixin, DetailView
):
    """Detail view for maintenance schemes (sub-module of maintenance app)"""

    model: MaintenanceType = MaintenanceType
    template_name: str = "maintenance/maintenance_schemes_detail.html"
    context_object_name: str = "scheme"
