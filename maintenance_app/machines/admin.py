from django.contrib import admin
from .models import Machine, MachineGroup


# class MachineAdmin(admin.ModelAdmin):
#     pass

admin.site.register(Machine)
admin.site.register(MachineGroup)
