from django.db import models
from machines.models.machine_group import MachineGroup


class MaintenanceType(models.Model):
    MAINTENANCE_TYPES: tuple[tuple[str]] = (
        ("week", "weekly maintenance"),
        ("month", "monthly maintenance"),
        ("half year", "half year maintenance"),
        ("year", "annual maintenance"),
        ("two-years", "two years maintenacne"),
        ("three-years", "three years maintenance"),
        ("additional", "non-standard maintenacne"),
    )
    type = models.CharField(
        max_length=50,
        choices=MAINTENANCE_TYPES,
        default="week",
        help_text="Maintenance type",
    )
    description = models.TextField(help_text="Description")
    machine_group = models.ForeignKey(
        MachineGroup, on_delete=models.CASCADE, default=0, help_text="Machine group"
    )

    def __str__(self):
        return f"{self.type}: {self.machine_group}"
