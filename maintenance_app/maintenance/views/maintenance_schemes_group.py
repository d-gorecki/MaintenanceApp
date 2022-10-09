from django.shortcuts import render
from django.views import View
from ..models import MaintenanceType


class MaintenanceSchemesGroup(View):
    def get(self, request, pk):
        schemes = MaintenanceType.objects.filter(machine_group=pk)
        context = {"schemes": schemes}

        return render(request, "maintenance/maintenance_schemes_group.html", context)
