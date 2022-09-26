from django.contrib import admin
from .models import MaintenanceType, MaintenanceSchedule, MaintenanceReport

admin.site.register(MaintenanceType)
admin.site.register(MaintenanceSchedule)
admin.site.register(MaintenanceReport)
