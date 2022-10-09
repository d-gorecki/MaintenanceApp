from django.shortcuts import redirect, render
from django.views import View
from ..forms import MaintenanceScheduleForm


class MaintenanceSchedulesAdd(View):
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
