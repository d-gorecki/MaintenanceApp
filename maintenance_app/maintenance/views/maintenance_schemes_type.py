from django.shortcuts import render
from django.views import View
from ..models import MaintenanceType


class MaintenanceSchemesType(View):
    def get(self, request, type):
        schemes = MaintenanceType.objects.filter(type=type)
        context = {"schemes": schemes}
        return render(request, "maintenance/maintenance_schemes_type.html", context)
