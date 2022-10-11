from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect
from django.views import View
from maintenance.forms.maintenance_schedule_form import MaintenanceScheduleForm
from maintenance.models.maintenance_schedule import MaintenanceSchedule


from maintenance_app.mixins import ManagerGroupTestMixin


class MaintenanceSchedulesEdit(LoginRequiredMixin, ManagerGroupTestMixin, View):
    """Update view for maintenance schedules (sub-module of maintenance app)"""

    template_name: str = "maintenance/maintenance_schedules_edit.html"
    form_class: MaintenanceScheduleForm = MaintenanceScheduleForm

    def get_schedule(self, pk: int) -> MaintenanceSchedule:
        return MaintenanceSchedule.objects.get(pk=pk)

    def get(self, request: HttpRequest, pk: int) -> HttpResponse:
        return render(
            request,
            self.template_name,
            {"form": self.form_class(instance=self.get_schedule(pk))},
        )

    def post(self, request: HttpRequest, pk: int) -> HttpResponse:
        form = self.form_class(request.POST, instance=self.get_schedule(pk))
        if form.is_valid():
            form.save()
            return redirect("/maintenance/schedules")
