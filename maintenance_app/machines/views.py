from django.shortcuts import render
from .models import Machine
from django.contrib.auth.decorators import login_required
from machines.models import Machine
from plotly.offline import plot
from plotly.graph_objs import Pie
from malfunctions.models import MalfunctionReport, ServiceReport
from maintenance.models import MaintenanceReport


@login_required()
def machines_comparison(request):
    if request.user.group == "production":
        machines = Machine.objects.filter(department=request.user.department)
    else:
        machines = Machine.objects.all()
    context = {"machines": machines}

    return render(request, "machines/machines_comparison.html", context)


def dashboard(request):
    labels = ["available", "nonworking"]
    values = [
        Machine.objects.filter(machine_status="available").count(),
        Machine.objects.filter(machine_status="nonwork").count(),
    ]
    plot_div = plot(
        [Pie(labels=labels, values=values, textinfo="label+percent")], output_type="div"
    )

    maintenances = MaintenanceReport.objects.all()

    context = {
        "plot_div": plot_div,
    }
    return render(request, "machines/dashboard.html", context)
