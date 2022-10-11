from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from ..forms import MaintenanceTypeForm
from maintenance.models.maintenance_type import MaintenanceType


from maintenance_app.mixins import ManagerGroupTestMixin


class MaintenanceSchemesEdit(LoginRequiredMixin, ManagerGroupTestMixin, View):
    """Update view for maintenance schemes (sub-module of maintenance app)"""

    form_class: MaintenanceTypeForm = MaintenanceTypeForm
    template_name: str = "maintenance/maintenance_schemes_edit.html"

    def get_scheme(self, pk: int) -> MaintenanceType:
        return MaintenanceType.objects.get(pk=pk)

    def get(self, request: HttpRequest, pk: int) -> HttpResponse:
        return render(
            request,
            self.template_name,
            {"form": self.form_class(instance=self.get_scheme(pk))},
        )

    def post(self, request: HttpRequest, pk: int) -> HttpResponse:
        form = self.form_class(request.POST, instance=self.get_scheme(pk))
        if form.is_valid():
            form.save()
            return redirect("/maintenance/")
