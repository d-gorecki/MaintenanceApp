from django.shortcuts import render
from .models import MaintenanceType


def maintenance_schemes(request):
    schemes = MaintenanceType.objects.all()
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
    pass
