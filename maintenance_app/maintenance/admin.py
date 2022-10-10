from django.contrib import admin
from .models import MaintenanceType, MaintenanceSchedule, MaintenanceReport


class AdminMaintenanceReport(admin.ModelAdmin):
    list_display: tuple[str] = ("id", "user", "schedule")
    search_fields: tuple[str] = ("user",)
    search_help_text: str = "user"


@admin.register(MaintenanceSchedule)
class AdminMaintenanceSchedule(admin.ModelAdmin):
    list_display: tuple[str] = ("machine", "maintenance_type", "planned_date", "user")
    search_fields: tuple[str] = ("machine",)
    search_help_text: str = "machine"


class AdminMaintenanceType(admin.ModelAdmin):
    list_display: tuple[str] = ("type", "description", "machine_group")
    search_fields: tuple[str] = ("type",)
    search_help_text: str = "maintenance type"


admin.site.register(MaintenanceType, AdminMaintenanceType)
admin.site.register(MaintenanceReport, AdminMaintenanceReport)
