from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import QuerySet
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from machines.models import Machine
from django.views import View


class Machines(LoginRequiredMixin, View):
    """Machines app main view, displaying all objects from Machine table"""

    def get(self, request: HttpRequest) -> HttpResponse:
        if request.user.group == "production":
            machines: QuerySet[Machine] = Machine.objects.filter(
                department=request.user.department
            )
        else:
            machines: QuerySet[Machine] = Machine.objects.all()
        context = {"machines": machines}

        return render(request, "machines/machines.html", context)
