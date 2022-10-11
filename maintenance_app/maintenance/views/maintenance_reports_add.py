from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.views import View
from maintenance.forms.maintenance_report_form import MaintenanceReportForm
from maintenance_app.mixins import ManagerMaintenanceGroupTestMixin


class MaintenanceReportsAdd(LoginRequiredMixin, ManagerMaintenanceGroupTestMixin, View):
    """Create view for maintenance reports (sub-module of maintenance app)"""

    form_class: MaintenanceReportForm = MaintenanceReportForm
    template_name: str = "maintenance/maintenance_reports_add.html"

    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, self.template_name, {"form": self.form_class()})

    def post(self, request: HttpRequest) -> HttpResponse:
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            report: MaintenanceReportForm = form.save(commit=False)
            report.user = request.user
            report.save()
            return redirect("/maintenance/schedules/reports/")
