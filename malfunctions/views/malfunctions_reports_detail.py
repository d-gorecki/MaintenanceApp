from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import View
from malfunctions.models.malfunction_report import MalfunctionReport


from maintenance_app.mixins import ManagerMaintenanceGroupTestMixin


class MalfunctionsReportsDetail(
    LoginRequiredMixin, ManagerMaintenanceGroupTestMixin, View
):
    """Detail view for malfunctions reports (sub-module of malfunctions app)"""

    template_name: str = "malfunctions/malfunctions_reports_detail.html"

    def get(self, request: HttpRequest, pk: int) -> HttpResponse:
        malfunction_report: MalfunctionReport = MalfunctionReport.objects.get(pk=pk)

        return render(
            request, self.template_name, {"malfunction_report": malfunction_report}
        )
