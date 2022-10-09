from django.views.generic import DetailView
from ..models import MaintenanceType


class MaintenanceSchemesDetail(DetailView):
    model = MaintenanceType
    template_name = "maintenance/maintenance_schemes_detail.html"
    context_object_name = "scheme"
