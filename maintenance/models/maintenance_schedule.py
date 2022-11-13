from django.conf import settings
from django.db import models

from machines.models.machine import Machine
from maintenance.models.maintenance_type import MaintenanceType


class MaintenanceSchedule(models.Model):
    STATUS = (
        ("pending", "pending"),
        ("done", "done"),
    )
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE, help_text="Machine")
    maintenance_type = models.ForeignKey(
        MaintenanceType, on_delete=models.CASCADE, help_text="Maintenance type"
    )
    planned_date = models.DateField(help_text="Maintenance planned date")
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        help_text="Responsible",
    )
    status = models.CharField(
        max_length=7,
        choices=STATUS,
        default="pending",
        help_text="Schedule status (" "pending/available",
    )

    def __str__(self):
        return f"{self.maintenance_type}: {self.planned_date}"
