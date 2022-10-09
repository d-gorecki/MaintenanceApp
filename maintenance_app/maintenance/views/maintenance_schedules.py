from django.shortcuts import render
from django.views import View
from maintenance.models import MaintenanceSchedule


class MaintenanceSchedules(View):
    def get(self, request):
        if request.user.group == "production":
            schedules = MaintenanceSchedule.objects.filter(
                machine__department=request.user.department
            )
        else:
            schedules = MaintenanceSchedule.objects.all()

        context = {"schedules": schedules}
        return render(request, "maintenance/maintenance_schedules.html", context)
