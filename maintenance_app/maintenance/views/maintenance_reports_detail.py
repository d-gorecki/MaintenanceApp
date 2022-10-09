from django.views.generic import DetailView
from ..models import MaintenanceReport


class MaintenanceReportsDetail(DetailView):
    model = MaintenanceReport
    template_name = "maintenance/maintenance_reports_detail.html"
