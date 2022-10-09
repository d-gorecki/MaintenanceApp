from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View
from ..forms import MaintenanceTypeForm
from ..models import MaintenanceType
from maintenance_app.mixins import ManagerGroupTestMixin


class MaintenanceSchemesEdit(LoginRequiredMixin, ManagerGroupTestMixin, View):
    form_class = MaintenanceTypeForm
    template_name = "maintenance/maintenance_schemes_edit.html"

    def get_scheme(self, pk):
        return MaintenanceType.objects.get(pk=pk)

    def get(self, request, pk):
        return render(
            request,
            self.template_name,
            {"form": self.form_class(instance=self.get_scheme(pk))},
        )

    def post(self, request, pk):
        form = self.form_class(request.POST, instance=self.get_scheme(pk))
        if form.is_valid():
            form.save()
            return redirect("/maintenance/")
