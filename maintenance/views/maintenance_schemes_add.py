from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.views import View

from maintenance.forms.maintenance_type_form import MaintenanceTypeForm
from maintenance_app.mixins import ManagerGroupTestMixin


class MaintenanceSchemesAdd(LoginRequiredMixin, ManagerGroupTestMixin, View):
    """Create view for maintenance schemes (sub-module of maintenance app)"""

    form_class: MaintenanceTypeForm = MaintenanceTypeForm
    template_name: str = "maintenance/maintenance_schemes_add.html"

    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, self.template_name, {"form": self.form_class()})

    def post(self, request: HttpRequest) -> HttpResponse:
        form: MaintenanceTypeForm = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/maintenance/")
