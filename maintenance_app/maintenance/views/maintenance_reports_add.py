from django.shortcuts import redirect, render
from django.views import View

from ..forms import MaintenanceReportForm


class MaintenanceReportsAdd(View):
    form_class = MaintenanceReportForm
    template_name = "maintenance/maintenance_reports_add.html"

    def get(self, request):
        return render(request, self.template_name, {"form": self.form_class()})

    def post(self, request):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            report = form.save(commit=False)
            report.user = request.user
            report.save()
            return redirect("/maintenance/schedules/reports/")
