from django.shortcuts import render, redirect
from .models import Machine
from django.contrib.auth.decorators import login_required
from plotly.offline import plot
from plotly.graph_objs import Pie
from malfunctions.models import MalfunctionReport, ServiceReport
from maintenance.models import MaintenanceReport
from .forms import MachineAddForm


@login_required()
def machines(request):
    if request.user.group == "production":
        machines = Machine.objects.filter(department=request.user.department)
    else:
        machines = Machine.objects.all()
    context = {"machines": machines}

    return render(request, "machines/machines.html", context)


def machines_add(request):
    if request.method == "POST":
        form = MachineAddForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("machines")

    form = MachineAddForm()
    context = {"form": form}

    return render(request, "machines/machines_add.html", context)


def machines_edit(request, pk):
    machine = Machine.objects.get(pk=pk)

    if request.method == "POST":
        form = MachineAddForm(request.POST, instance=machine)
        if form.is_valid():
            form.save()
            return redirect("machines")

    form = MachineAddForm(instance=machine)
    context = {"form": form}

    return render(request, "machines/machines_edit.html", context)
