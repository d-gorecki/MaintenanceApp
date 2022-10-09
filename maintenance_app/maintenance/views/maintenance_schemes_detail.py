from django.views.generic import DetailView
from ..models import MaintenanceType


class MaintenanceSchemesDetail(DetailView):
    model = MaintenanceType
