from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import View

from maintenance_app.mixins import ManagerMaintenanceGroupTestMixin
from malfunctions.models.service_report import ServiceReport


class MalfunctionsServicesDetail(
    LoginRequiredMixin, ManagerMaintenanceGroupTestMixin, View
):
    """Detail view for malfunctions services (sub-module of malfunctions app)"""

    template_name: str = "malfunctions/malfunctions_services_detail.html"

    def get(self, request: HttpRequest, pk: int) -> HttpResponse:
        services_report: ServiceReport = ServiceReport.objects.get(pk=pk)
        return render(request, self.template_name, {"services_report": services_report})
