from django.db import models
from .machine_group import MachineGroup
from departments.models import Department


class Machine(models.Model):
    STATUS = (
        ("available", "working fine"),
        ("malfunction", "not working"),
    )

    factory_number = models.CharField(max_length=100, help_text="Factory number")
    machine_group = models.ForeignKey(
        MachineGroup, on_delete=models.CASCADE, help_text="Machine group"
    )
    name = models.CharField(max_length=100, help_text="Machine name(model)")
    number = models.CharField(max_length=100, help_text="Department number")
    producer = models.CharField(max_length=100, help_text="Producer")
    purchase_data = models.DateField(help_text="Purchase date", blank=True, null=True)
    department = models.ForeignKey(
        Department, on_delete=models.CASCADE, help_text="Department"
    )
    machine_status = models.CharField(
        max_length=32,
        choices=STATUS,
        default="available",
        help_text="Machine status (available/not working)",
    )

    def __str__(self):
        return f"{self.factory_number}: {self.name}"
