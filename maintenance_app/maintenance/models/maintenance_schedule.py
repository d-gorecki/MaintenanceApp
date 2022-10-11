from django.db import models
from machines.models.machine import Machine
from django.conf import settings
from maintenance.models.maintenance_type import MaintenanceType


class MaintenanceSchedule(models.Model):
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE, help_text="Machine")
    maintenance_type = models.ForeignKey(
        MaintenanceType, on_delete=models.CASCADE, help_text="Maintenance type"
    )
    planned_date = models.DateField(help_text="Maintenance planned date")
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_DEFAULT,
        default=0,
        help_text="Responsible",
    )
    # on user deletion app should reassign another user to planned maintenance

    def __str__(self):
        return f"{self.maintenance_type}: {self.planned_date}"
