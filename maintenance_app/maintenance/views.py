from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import MaintenanceType, MaintenanceSchedule, MaintenanceReport
from .forms import MaintenanceTypeForm, MaintenanceScheduleForm, MaintenanceReportForm
from users.models import User

# TODO CLASS BASED VIEW -> INSTEAD OF SIMPLES FUNCTIONS?METHODS, DIFFERENT FILES, PACKAGE OF VIEWS CLASSES.


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


def maintenance_schedules(request):
    if request.user.group == "production":
        schedules = MaintenanceSchedule.objects.filter(
            machine__department=request.user.department
        )
    else:
        schedules = MaintenanceSchedule.objects.all()
    context = {"schedules": schedules}

    return render(request, "maintenance/maintenance_schedules.html", context)


def maintenance_schedules_add(request):
    form = MaintenanceScheduleForm()

    if request.method == "POST":
        form = MaintenanceScheduleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/maintenance/schedules/")

    context = {"form": form}

    return render(request, "maintenance/maintenance_schedules_add.html", context)


def maintenance_schedules_edit(request, pk):
    schedule = MaintenanceSchedule.objects.get(pk=pk)
    form = MaintenanceScheduleForm(instance=schedule)

    if request.method == "POST":
        form = MaintenanceScheduleForm(request.POST, instance=schedule)
        if form.is_valid():
            form.save()
            return redirect("/maintenance/schedules")

    context = {"form": form}
    return render(request, "maintenance/maintenance_schedules_edit.html", context)


def maintenance_reports(request):
    reports = MaintenanceReport.objects.all()

    context = {"reports": reports}
    return render(request, "maintenance/maintenance_reports.html", context)


def maintenance_reports_detail(request, pk):
    report = MaintenanceReport.objects.get(pk=pk)

    context = {"report": report}
    return render(request, "maintenance/maintenance_reports_detail.html", context)


def maintenance_reports_add(request):
    form = MaintenanceReportForm()

    if request.method == "POST":
        form = MaintenanceReportForm(request.POST, request.FILES)
        if form.is_valid():
            report = form.save(commit=False)
            report.user = request.user
            report.save()
            return redirect("/maintenance/schedules/reports/")

    context = {"form": form}
    return render(request, "maintenance/maintenance_reports_add.html", context)
