from django.contrib import admin
from .models import Department


class AdminDepartment(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)
    search_help_text = "name"


admin.site.register(Department, AdminDepartment)
