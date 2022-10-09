from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View
from ..models import MaintenanceType
from maintenance_app.mixins import ManagerMaintenanceGroupTestMixin


class MaintenanceSchemesGroup(
    LoginRequiredMixin, ManagerMaintenanceGroupTestMixin, View
):
    def get(self, request, pk):
        schemes = MaintenanceType.objects.filter(machine_group=pk)
        context = {"schemes": schemes}

        return render(request, "maintenance/maintenance_schemes_group.html", context)
