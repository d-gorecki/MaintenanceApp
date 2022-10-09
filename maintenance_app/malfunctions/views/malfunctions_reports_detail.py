from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View
from ..models import MalfunctionReport
from maintenance_app.mixins import ManagerMaintenanceGroupTestMixin


class MalfunctionsReportsDetail(
    LoginRequiredMixin, ManagerMaintenanceGroupTestMixin, View
):
    template_name = "malfunctions/malfunctions_reports_detail.html"

    def get(self, request, pk):
        malfunction_report = MalfunctionReport.objects.get(pk=pk)

        return render(
            request, self.template_name, {"malfunction_report": malfunction_report}
        )
