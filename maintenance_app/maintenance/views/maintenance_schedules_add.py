from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.views import View
from maintenance.forms.maintenance_schedule_form import MaintenanceScheduleForm
from maintenance_app.mixins import ManagerGroupTestMixin


class MaintenanceSchedulesAdd(LoginRequiredMixin, ManagerGroupTestMixin, View):
    """Create view for maintenance schedules (sub-module of maintenance app)"""

    form_class: MaintenanceScheduleForm = MaintenanceScheduleForm
    template_name: str = "maintenance/maintenance_schedules_add.html"

    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, self.template_name, {"form": self.form_class()})

    def post(self, request: HttpRequest) -> HttpResponse:
        if request.method == "POST":
            form: MaintenanceScheduleForm = self.form(request.POST)
            if form.is_valid():
                form.save()
                return redirect("/maintenance/schedules/")
