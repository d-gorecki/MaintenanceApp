from django.db.models import QuerySet
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from django.views import View
from maintenance.models.maintenance_schedule import MaintenanceSchedule


class MaintenanceSchedules(View):
    """Base view for maintenance schedules (sub-module of maintenance app)"""

    def get(self, request: HttpRequest) -> HttpResponse:
        if request.user.group == "production":
            schedules: QuerySet[
                MaintenanceSchedule
            ] = MaintenanceSchedule.objects.filter(
                machine__department=request.user.department, status="pending"
            )
        else:
            schedules: QuerySet[
                MaintenanceSchedule
            ] = MaintenanceSchedule.objects.filter(status="pending")

        context: dict[str, QuerySet[MaintenanceSchedule]] = {"schedules": schedules}
        return render(request, "maintenance/maintenance_schedules.html", context)
