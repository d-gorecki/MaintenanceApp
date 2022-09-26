from django.shortcuts import render
from .models import MalfunctionReport, MalfunctionPending


def malfunctions_pending(request):
    malfunctions = MalfunctionPending.objects.all()
    context = {"malfunctions": malfunctions}

    return render(request, "malfunctions/malfunctions_pending.html", context)
