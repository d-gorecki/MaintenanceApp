from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from machines.models import Machine
from django.views import View


class Machines(LoginRequiredMixin, View):
    """Machines app main view"""

    def get(self, request):
        if request.user.group == "production":
            machines = Machine.objects.filter(department=request.user.department)
        else:
            machines = Machine.objects.all()
        context = {"machines": machines}

        return render(request, "machines/machines.html", context)
