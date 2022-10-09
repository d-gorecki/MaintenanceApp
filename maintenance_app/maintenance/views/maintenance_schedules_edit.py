from django.shortcuts import render, redirect
from django.views import View
from ..forms import MaintenanceScheduleForm
from ..models import MaintenanceSchedule


class MaintenanceSchedulesEdit(View):
    template_name = "maintenance/maintenance_schedules_edit.html"
    form_class = MaintenanceScheduleForm

    def get_schedule(self, pk):
        return MaintenanceSchedule.objects.get(pk=pk)

    def get(self, request, pk):
        return render(
            request,
            self.template_name,
            {"form": self.form_class(instance=self.get_schedule(pk))},
        )

    def post(self, request, pk):
        form = self.form_class(request.POST, instance=self.get_schedule(pk))
        if form.is_valid():
            form.save()
            return redirect("/maintenance/schedules")
