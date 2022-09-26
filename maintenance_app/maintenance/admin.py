from django.contrib import admin
from .models import MaintenanceType, MaintenanceSchedule

admin.site.register(MaintenanceType)
admin.site.register(MaintenanceSchedule)
