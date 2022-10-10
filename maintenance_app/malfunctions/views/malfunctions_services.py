from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import QuerySet
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import View
from ..models import ServiceReport
from maintenance_app.mixins import ManagerMaintenanceGroupTestMixin


class MalfunctionsServices(LoginRequiredMixin, ManagerMaintenanceGroupTestMixin, View):
    """Base view for malfunctions services (sub-module of malfunctions app)"""

    template_name: str = "malfunctions/malfunctions_services.html"

    def get(self, request: HttpRequest) -> HttpResponse:
        services: QuerySet[ServiceReport] = ServiceReport.objects.all()
        return render(request, self.template_name, {"services": services})
