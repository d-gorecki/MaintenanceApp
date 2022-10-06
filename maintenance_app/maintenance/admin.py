from django.contrib import admin
from .models import MaintenanceType, MaintenanceSchedule, MaintenanceReport


class AdminMaintenanceReport(admin.ModelAdmin):
    list_display = ("id", "user", "schedule")
    search_fields = ("user",)


admin.site.register(MaintenanceReport, AdminMaintenanceReport)


admin.site.register(MaintenanceType)
admin.site.register(MaintenanceSchedule)
