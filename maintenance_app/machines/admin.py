from django.contrib import admin
from .models import Machine, MachineGroup


@admin.register(Machine)
class MachineAdmin(admin.ModelAdmin):
    search_fields = ("factory_number",)
    search_help_text = "factory number"


@admin.register(MachineGroup)
class MachineGroupAdmin(admin.ModelAdmin):
    search_fields = ("group",)
    search_help_text = "group"
