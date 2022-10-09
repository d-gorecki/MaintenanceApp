from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View
from ..models import MaintenanceType
from maintenance_app.mixins import ManagerMaintenanceGroupTestMixin


class MaintenanceSchemesType(
    LoginRequiredMixin, ManagerMaintenanceGroupTestMixin, View
):
    def get(self, request, type):
        schemes = MaintenanceType.objects.filter(type=type)
        context = {"schemes": schemes}
        return render(request, "maintenance/maintenance_schemes_type.html", context)
