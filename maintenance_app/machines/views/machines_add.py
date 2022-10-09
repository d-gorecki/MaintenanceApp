from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.views import View
from machines.forms import MachineAddForm


class MachinesAdd(LoginRequiredMixin, View):
    form_class = MachineAddForm
    template_name = "machines/machines_add.html"

    def get(self, request):
        form = self.form_class()
        context = {"form": form}
        return render(request, self.template_name, context)

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect("machines")

        return render(request, self.template_name, {"form": form})
