from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import QuerySet
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import View

# from machines.models import Machine
from machines.models.machine import Machine


class Machines(LoginRequiredMixin, View):
    """Machines app main view, displaying all objects from Machine table"""

    def get(self, request: HttpRequest) -> HttpResponse:
        if request.user.group == "production":
            machines: QuerySet[Machine] = Machine.objects.filter(
                department=request.user.department
            )
        else:
            machines: QuerySet[Machine] = Machine.objects.all()
        context: dict[str, QuerySet[Machine]] = {"machines": machines}

        return render(request, "machines/machines.html", context)
