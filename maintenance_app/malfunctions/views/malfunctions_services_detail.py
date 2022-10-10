from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from django.views import View
from ..models import ServiceReport
from maintenance_app.mixins import ManagerMaintenanceGroupTestMixin


class MalfunctionsServicesDetail(
    LoginRequiredMixin, ManagerMaintenanceGroupTestMixin, View
):
    """Detail view for malfunctions services (sub-module of malfunctions app)"""

    template_name: str = "malfunctions/malfunctions_services_detail.html"

    def get(self, request: HttpRequest, pk: int) -> HttpResponse:
        services_report: ServiceReport = ServiceReport.objects.get(pk=pk)
        return render(request, self.template_name, {"services_report": services_report})
