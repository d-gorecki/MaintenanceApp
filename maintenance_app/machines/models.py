from django.db import models
from departments.models import Department


class MachineGroup(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Machine(models.Model):
    STATUS = (
        ("available", "working fine"),
        ("nonwork", "not working"),
        ("attention", "need some repairs but working"),
    )

    factory_number = models.CharField(max_length=100)
    machine_group = models.ForeignKey(MachineGroup, on_delete=models.CASCADE, default=0)
    name = models.CharField(max_length=100)
    number = models.CharField(max_length=100)
    producer = models.CharField(max_length=100)
    purchase_data = models.DateField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    machine_status = models.CharField(
        max_length=32, choices=STATUS, default="available"
    )

    def __str__(self):
        return f"{self.factory_number}: {self.name}"
