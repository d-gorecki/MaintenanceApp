from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View
from ..models import MaintenanceType
from maintenance_app.mixins import ManagerMaintenanceGroupTestMixin


class MaintenanceSchemes(LoginRequiredMixin, ManagerMaintenanceGroupTestMixin, View):
    template_name = "maintenance/maintenance_schemes.html"
    schemes = MaintenanceType.objects.all()

    def get(self, request):
        return render(request, self.template_name, {"schemes": self.schemes})
