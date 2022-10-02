from django.shortcuts import render, redirect
from .models import MalfunctionReport, MalfunctionPending
from .forms import ReportForm
from users.models import User


def malfunctions_pending(request):
    malfunctions = MalfunctionPending.objects.all()
    context = {"malfunctions": malfunctions}

    return render(request, "malfunctions/malfunctions_pending.html", context)


def malfunctions_report(request):
    form = ReportForm()
    user = User.objects.first()  # TODO: pass logged user

    if request.method == "POST":
        form = ReportForm(request.POST)
        if form.is_valid():
            malfunction_report = MalfunctionReport(
                machine=form.cleaned_data.get("machine"),
                user=user,
                description=form.cleaned_data.get("description"),
                image=form.cleaned_data.get("image"),
            )
            malfunction_report.save()
            return redirect("/malfunctions/pending")

    context = {"form": form}

    return render(request, "malfunctions/malfunctions_report.html", context)
