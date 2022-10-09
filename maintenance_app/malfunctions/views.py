from django.shortcuts import render, redirect, HttpResponse
from .models import MalfunctionReport, MalfunctionPending, ServiceReport
from .forms import ReportForm, ServiceReportForm
from users.models import User
from machines.models import Machine


# TODO typing, docstring


def malfunctions_pending(request):
    malfunctions = MalfunctionReport.objects.filter(status="pending")
    context = {"malfunctions": malfunctions}

    return render(request, "malfunctions/malfunctions_pending.html", context)


def malfunctions_reports_add(request):
    machine = request.GET.get("machine")
    if machine:
        form = ReportForm(initial={"machine": machine}, user=request.user)
    else:
        form = ReportForm(user=request.user)

    if request.method == "POST":
        form = ReportForm(request.POST, request.FILES, user=request.user)
        if form.is_valid():
            report = form.save(commit=False)
            report.user = request.user
            report.save()
            return redirect("/malfunctions/pending")
        else:
            return HttpResponse(f"<h1>{form.errors}</h1>")

    context = {"form": form}

    return render(request, "malfunctions/malfunctions_reports_add.html", context)


def malfunctions_reports(request):
    malfunction_reports = MalfunctionReport.objects.all().order_by("-id")
    context = {"malfunction_reports": malfunction_reports}

    return render(request, "malfunctions/malfunctions_reports.html", context)


def malfunctions_reports_detail(request, pk):
    malfunction_report = MalfunctionReport.objects.get(pk=pk)
    context = {"malfunction_report": malfunction_report}

    return render(request, "malfunctions/malfunctions_reports_detail.html", context)


def malfunctions_services(request):
    services = ServiceReport.objects.all()
    context = {"services": services}

    return render(request, "malfunctions/malfunctions_services.html", context)


def malfunctions_services_detail(request, pk):
    services_report = ServiceReport.objects.get(pk=pk)
    context = {"services_report": services_report}

    return render(request, "malfunctions/malfunctions_services_detail.html", context)


def malfunctions_services_add(request):
    malfunction = request.GET.get("malfunction")
    if malfunction:
        form = ServiceReportForm(initial={"malfunction_report": malfunction})
    else:
        form = ServiceReportForm()

    if request.method == "POST":
        form = ServiceReportForm(request.POST, request.FILES)
        if form.is_valid():
            report = form.save(commit=False)
            report.user = request.user
            report.save()
            return redirect("/malfunctions/services")
        else:
            return HttpResponse(f"<h1>{form.errors}</h1>")

    context = {"form": form}

    return render(request, "malfunctions/malfunctions_services_add.html", context)
