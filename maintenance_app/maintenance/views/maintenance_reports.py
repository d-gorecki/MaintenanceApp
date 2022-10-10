from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import QuerySet
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import View
from ..models import MaintenanceReport
from maintenance_app.mixins import ManagerMaintenanceGroupTestMixin


class MaintenanceReports(LoginRequiredMixin, ManagerMaintenanceGroupTestMixin, View):
    """Base view for maintenance reports (maintenance app sub-module)"""

    template_name: str = "maintenance/maintenance_reports.html"
    reports: QuerySet[MaintenanceReport] = MaintenanceReport.objects.all()

    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, self.template_name, {"reports": self.reports})
