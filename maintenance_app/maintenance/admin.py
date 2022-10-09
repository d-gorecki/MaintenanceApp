from django.contrib import admin
from .models import MaintenanceType, MaintenanceSchedule, MaintenanceReport


class AdminMaintenanceReport(admin.ModelAdmin):
    list_display = ("id", "user", "schedule")
    search_fields = ("user",)
    search_help_text = "user"


@admin.register(MaintenanceSchedule)
class AdminMaintenanceSchedule(admin.ModelAdmin):
    list_display = ("machine", "maintenance_type", "planned_date", "user")
    search_fields = ("machine",)
    search_help_text = "machine"


class AdminMaintenanceType(admin.ModelAdmin):
    list_display = ("type", "description", "machine_group")
    search_fields = ("type",)
    search_help_text = "maintenance type"


admin.site.register(MaintenanceType, AdminMaintenanceType)
admin.site.register(MaintenanceReport, AdminMaintenanceReport)
