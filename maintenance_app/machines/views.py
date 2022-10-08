from django.shortcuts import render
from .models import Machine
from django.contrib.auth.decorators import login_required


@login_required()
def machines_comparison(request):
    if request.user.group == "production":
        machines = Machine.objects.filter(department=request.user.department)
    else:
        machines = Machine.objects.all()
    context = {"machines": machines}

    return render(request, "machines/machines_comparison.html", context)
