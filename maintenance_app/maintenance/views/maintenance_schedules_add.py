from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.views import View
from ..forms import MaintenanceScheduleForm
from maintenance_app.mixins import ManagerGroupTestMixin


class MaintenanceSchedulesAdd(LoginRequiredMixin, ManagerGroupTestMixin, View):
    form_class = MaintenanceScheduleForm
    template_name = "maintenance/maintenance_schedules_add.html"

    def get(self, request):
        return render(request, self.template_name, {"form": self.form_class()})

    def post(self, request):
        if request.method == "POST":
            form = self.form(request.POST)
            if form.is_valid():
                form.save()
                return redirect("/maintenance/schedules/")
