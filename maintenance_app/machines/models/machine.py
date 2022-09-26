from django.db import models
from departments.models import Department


class Machine(models.Model):
    STATUS = (
        ("available", "working fine"),
        ("nonwork", "not working"),
        ("attention", "need some repairs but working"),
    )

    factory_number = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    number = models.CharField(max_length=100)
    producer = models.CharField(max_length=100)
    purchase_data = models.DateField()
    status = models.CharField(max_length=32, choices=STATUS, default="available")
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
