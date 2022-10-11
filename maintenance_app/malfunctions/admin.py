from django.contrib import admin
from .models import MalfunctionReport, ServiceReport


@admin.register(MalfunctionReport)
class AdminMalfunctionReport(admin.ModelAdmin):
    list_display: tuple[str] = ("machine", "user", "datetime", "description", "status")
    search_fields: tuple[str] = ("machine",)
    search_help_text: str = "machine"


@admin.register(ServiceReport)
class AdminServiceReport(admin.ModelAdmin):
    list_display: tuple[str] = (
        "malfunction_report",
        "user",
        "datetime",
        "description",
        "service",
    )
    search_fields: tuple[str] = ("malfunction_report",)
    search_help_text: str = "malfunction_report"
