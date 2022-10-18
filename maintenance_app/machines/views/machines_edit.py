from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.views import View
from machines.forms import MachineAddForm

from machines.models.machine import Machine

from maintenance_app.mixins import ManagerGroupTestMixin


class MachinesEdit(LoginRequiredMixin, ManagerGroupTestMixin, View):
    """Machines app edit view (edit existing machine)"""

    form_class: MachineAddForm = MachineAddForm
    template_name: str = "machines/machines_edit.html"

    def get(self, request: HttpRequest, pk: int) -> HttpResponse:
        instance: Machine = Machine.objects.get(pk=pk)
        form: MachineAddForm = self.form_class(instance=instance)
        context: dict[str, MachineAddForm] = {"form": form}
        return render(request, self.template_name, context)

    def post(self, request: HttpRequest, pk: int) -> HttpResponse:
        instance: Machine = Machine.objects.get(pk=pk)
        form: MachineAddForm = self.form_class(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect("machines")

        return render(request, self.template_name, {"form": form})
