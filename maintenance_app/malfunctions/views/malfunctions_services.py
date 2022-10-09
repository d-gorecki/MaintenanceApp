from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View
from ..models import ServiceReport
from maintenance_app.mixins import ManagerMaintenanceGroupTestMixin


class MalfunctionsServices(LoginRequiredMixin, ManagerMaintenanceGroupTestMixin, View):
    template_name = "malfunctions/malfunctions_services.html"

    def get(self, request):
        services = ServiceReport.objects.all()
        return render(request, self.template_name, {"services": services})
