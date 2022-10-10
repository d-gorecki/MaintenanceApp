from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import QuerySet
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from django.views import View
from ..models import MaintenanceType
from maintenance_app.mixins import ManagerMaintenanceGroupTestMixin


class MaintenanceSchemes(LoginRequiredMixin, ManagerMaintenanceGroupTestMixin, View):
    """Base view for maintenance schemes (sub-module of maintenance app)"""

    template_name: str = "maintenance/maintenance_schemes.html"
    schemes: QuerySet[MaintenanceType] = MaintenanceType.objects.all()

    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, self.template_name, {"schemes": self.schemes})
