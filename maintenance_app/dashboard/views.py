from typing import Union

from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import QuerySet
from django.shortcuts import render
from plotly.offline import plot
from plotly.graph_objs import Pie
from malfunctions.models import MalfunctionReport, ServiceReport
from maintenance.models import MaintenanceReport
from machines.models import Machine
from django.views import View
from maintenance_app.mixins import ManagerGroupTestMixin
from django.http import HttpRequest, HttpResponse


class Dashboard(LoginRequiredMixin, ManagerGroupTestMixin, View):
    """Dashboard class-based view. Access restricted only to users with manager group.
    Consist of 4 sub-views(divs): 1. pie-chart (working/not working machines), 2. Three latest
    malfunction reports. 3. Three latest maintenance reports. 4. Three latest service reports."""

    def get(self, request: HttpRequest) -> HttpResponse:
        labels: list[str] = ["available", "nonworking"]
        values: list[int] = [
            Machine.objects.filter(machine_status="available").count(),
            Machine.objects.filter(machine_status="nonwork").count(),
        ]
        plot_div: str = plot(
            [Pie(labels=labels, values=values, textinfo="label+percent")],
            output_type="div",
        )

        malfunctions_reports: QuerySet[
            MalfunctionReport
        ] = MalfunctionReport.objects.all().order_by("-id")[:3]
        maintenance_reports: QuerySet[
            MaintenanceReport
        ] = MaintenanceReport.objects.all().order_by("-id")[:3]
        malfunctions_services: QuerySet[
            ServiceReport
        ] = ServiceReport.objects.all().order_by("-id")[:3]

        context: dict[
            str,
            Union[
                str,
                QuerySet[Union[MalfunctionReport, MaintenanceReport, ServiceReport]],
            ],
        ] = {
            "plot_div": plot_div,
            "malfunctions_reports": malfunctions_reports,
            "maintenance_reports": maintenance_reports,
            "malfunctions_services": malfunctions_services,
        }
        return render(request, "dashboard/dashboard.html", context)
