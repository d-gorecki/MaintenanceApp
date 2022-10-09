from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.views import View
from machines.forms import MachineAddForm
from machines.models import Machine

from maintenance_app.mixins import ManagerGroupTestMixin


class MachinesEdit(LoginRequiredMixin, ManagerGroupTestMixin, View):
    form_class = MachineAddForm
    template_name = "machines/machines_edit.html"

    def get(self, request, pk):
        instance = Machine.objects.get(pk=pk)
        form = self.form_class(instance=instance)
        context = {"form": form}
        return render(request, self.template_name, context)

    def post(self, request, pk):
        instance = Machine.objects.get(pk=pk)
        form = self.form_class(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect("machines")

        return render(request, self.template_name, {"form": form})
