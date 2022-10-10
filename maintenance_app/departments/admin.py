from django.contrib import admin
from .models import Department


class AdminDepartment(admin.ModelAdmin):
    list_display: tuple[str, str] = ("id", "name")
    search_fields: tuple[str] = ("name",)
    search_help_text: str = "name"


admin.site.register(Department, AdminDepartment)
