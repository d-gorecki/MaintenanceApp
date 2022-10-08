from django.shortcuts import render
from plotly.offline import plot
from plotly.graph_objs import Pie
from malfunctions.models import MalfunctionReport, ServiceReport
from maintenance.models import MaintenanceReport
from machines.models import Machine


def dashboard(request):
    labels = ["available", "nonworking"]
    values = [
        Machine.objects.filter(machine_status="available").count(),
        Machine.objects.filter(machine_status="nonwork").count(),
    ]
    plot_div = plot(
        [Pie(labels=labels, values=values, textinfo="label+percent")], output_type="div"
    )

    malfunctions_reports = MalfunctionReport.objects.all().order_by("-id")[:3]
    maintenance_reports = MaintenanceReport.objects.all().order_by("-id")[:3]
    malfunctions_services = ServiceReport.objects.all().order_by("-id")[:3]

    context = {
        "plot_div": plot_div,
        "malfunctions_reports": malfunctions_reports,
        "maintenance_reports": maintenance_reports,
        "malfunctions_services": malfunctions_services,
    }
    return render(request, "dashboard/dashboard.html", context)
