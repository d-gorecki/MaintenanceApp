from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import QuerySet
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from django.views import View
from maintenance.models.maintenance_type import MaintenanceType


from maintenance_app.mixins import ManagerMaintenanceGroupTestMixin


class MaintenanceSchemesGroup(
    LoginRequiredMixin, ManagerMaintenanceGroupTestMixin, View
):
    """Group-filtered view for maintenance schemes (sub-module of maintenance app)"""

    def get(self, request: HttpRequest, pk: int) -> HttpResponse:
        schemes: QuerySet[MaintenanceType] = MaintenanceType.objects.filter(
            machine_group=pk
        )
        context: dict[str, QuerySet[MaintenanceType]] = {"schemes": schemes}

        return render(request, "maintenance/maintenance_schemes_group.html", context)
