from django.shortcuts import render
from django.views import View
from ..models import MaintenanceReport


class MaintenanceReports(View):
    template_name = "maintenance/maintenance_reports.html"
    reports = MaintenanceReport.objects.all()

    def get(self, request):
        return render(request, self.template_name, {"reports": self.reports})
