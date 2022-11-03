from django.contrib import admin

# from .models import Machine, MachineGroup
from machines.models.machine import Machine
from machines.models.machine_group import MachineGroup


@admin.register(Machine)
class MachineAdmin(admin.ModelAdmin):
    search_fields: tuple[str] = ("factory_number",)
    search_help_text: str = "factory number"


@admin.register(MachineGroup)
class MachineGroupAdmin(admin.ModelAdmin):
    search_fields: tuple[str] = ("group",)
    search_help_text: str = "group"
