from django.shortcuts import render
from .models import Machine


def machines_comparison(request):
    machines = Machine.objects.all()
    context = {"machines": machines}

    return render(request, "machines/machines_comparison.html", context)
