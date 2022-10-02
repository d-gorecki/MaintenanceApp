from django.shortcuts import render, redirect
from .models import MaintenanceType
from .forms import MaintenanceTypeForm


def maintenance_schemes(request):
    schemes = MaintenanceType.objects.all().order_by("pk")
    context = {"schemes": schemes}

    return render(request, "maintenance/maintenance_schemes.html", context)


def maintenance_schemes_detail(request, pk):
    scheme = MaintenanceType.objects.get(id=pk)
    context = {"scheme": scheme}

    return render(request, "maintenance/maintenance_schemes_detail.html", context)


def maintenance_schemes_group(request, pk):
    schemes = MaintenanceType.objects.filter(machine_group=pk)
    context = {"schemes": schemes}

    return render(request, "maintenance/maintenance_schemes_group.html", context)


def maintenance_schemes_type(request, type):
    schemes = MaintenanceType.objects.filter(type=type)
    context = {"schemes": schemes}

    return render(request, "maintenance/maintenance_schemes_type.html", context)


def maintenance_schemes_add(request):
    form = MaintenanceTypeForm()

    if request.method == "POST":
        form = MaintenanceTypeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/maintenance/")

    context = {"form": form}

    return render(request, "maintenance/maintenance_schemes_add.html", context)


def maintenance_schemes_edit(
    request, pk
):  # TODO: create reusable maintenance_schemes_add class and inherit it by edit class
    scheme = MaintenanceType.objects.get(pk=pk)
    form = MaintenanceTypeForm(instance=scheme)

    if request.method == "POST":
        form = MaintenanceTypeForm(request.POST, instance=scheme)
        if form.is_valid():
            form.save()
            return redirect("/maintenance/")

    context = {"form": form}

    return render(request, "maintenance/maintenance_schemes_edit.html", context)
