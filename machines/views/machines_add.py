from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.views import View

from machines.forms import MachineAddForm
from maintenance_app.mixins import ManagerGroupTestMixin


class MachinesAdd(LoginRequiredMixin, ManagerGroupTestMixin, View):
    """Machines app create view (add new machine)"""

    form_class: MachineAddForm = MachineAddForm
    template_name: str = "machines/machines_add.html"

    def get(self, request: HttpRequest) -> HttpResponse:
        form: MachineAddForm = self.form_class()
        context: dict[str, MachineAddForm] = {"form": form}
        return render(request, self.template_name, context)

    def post(self, request: HttpRequest) -> HttpResponse:
        form: MachineAddForm = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect("machines")

        return render(request, self.template_name, {"form": form})
