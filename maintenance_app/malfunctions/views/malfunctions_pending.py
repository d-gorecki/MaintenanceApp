from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import QuerySet
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import View

from malfunctions.models.malfunction_report import MalfunctionReport

from maintenance_app.mixins import ManagerMaintenanceGroupTestMixin


class MalfunctionsPending(LoginRequiredMixin, ManagerMaintenanceGroupTestMixin, View):
    """Base view for malfunctions pending (sub-module of malfunctions app)"""

    template_name: str = "malfunctions/malfunctions_pending.html"

    def get(self, request: HttpRequest) -> HttpResponse:
        malfunctions: QuerySet[MalfunctionReport] = MalfunctionReport.objects.filter(
            status="pending"
        )
        return render(request, self.template_name, {"malfunctions": malfunctions})
