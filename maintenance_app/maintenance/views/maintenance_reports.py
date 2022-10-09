from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View
from ..models import MaintenanceReport
from maintenance_app.mixins import ManagerMaintenanceGroupTestMixin


class MaintenanceReports(LoginRequiredMixin, ManagerMaintenanceGroupTestMixin, View):
    template_name = "maintenance/maintenance_reports.html"
    reports = MaintenanceReport.objects.all()

    def get(self, request):
        return render(request, self.template_name, {"reports": self.reports})
