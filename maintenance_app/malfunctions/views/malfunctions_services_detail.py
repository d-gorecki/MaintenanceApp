from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View
from ..models import ServiceReport
from maintenance_app.mixins import ManagerMaintenanceGroupTestMixin


class MalfunctionsServicesDetail(
    LoginRequiredMixin, ManagerMaintenanceGroupTestMixin, View
):
    template_name = "malfunctions/malfunctions_services_detail.html"

    def get(self, request, pk):
        services_report = ServiceReport.objects.get(pk=pk)
        return render(request, self.template_name, {"services_report": services_report})
