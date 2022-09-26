from django.db import models
from machines.models import MachineGroup


class MaintenanceType(models.Model):
    MAINTENANCE_TYPES = (
        ("week", "weekly maintenance"),
        ("month", "monthly maintenance"),
        ("half year", "half year maintenance"),
        ("year", "annual maintenance"),
        ("two years", "two years maintenacne"),
        ("three years", "three years maintenance"),
        ("additional", "non-standard maintenacne"),
    )
    type = models.CharField(max_length=50, choices=MAINTENANCE_TYPES, default="week")
    description = models.TextField()
    machine_group = models.ForeignKey(MachineGroup, on_delete=models.CASCADE, default=0)
