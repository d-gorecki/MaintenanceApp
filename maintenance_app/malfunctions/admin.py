from django.contrib import admin
from .models import MalfunctionReport, MalfunctionPending, ServiceReport


@admin.register(MalfunctionReport)
class AdminMalfunctionReport(admin.ModelAdmin):
    list_display = ("machine", "user", "datetime", "description", "status")
    search_fields = ("machine",)
    search_help_text = "machine"


@admin.register(ServiceReport)
class AdminServiceReport(admin.ModelAdmin):
    list_display = ("malfunction_report", "user", "datetime", "description", "service")
    search_fields = ("malfunction_report",)
    search_help_text = "malfunction_report"


admin.site.register(MalfunctionPending)
