from django.contrib.auth.models import User
from django.db import models
from machines.models import Machine
from django.conf import settings


class MalfunctionReport(models.Model):
    STATUS = (("pending", "pending"), ("finished", "finished"))

    machine = models.ForeignKey(Machine, on_delete=models.CASCADE)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_DEFAULT, default=0
    )
    datetime = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    image = models.ImageField(upload_to="media/malfunction_issues")
    status = models.CharField(max_length=8, choices=STATUS, default="pending")

    def __str__(self):
        return f"#{self.pk}-{self.machine}"


class MalfunctionPending(models.Model):
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE)
    malfunction_report = models.OneToOneField(
        MalfunctionReport, on_delete=models.CASCADE
    )

    # prop unnecessary model


class ServiceReport(models.Model):
    malfunction_report = models.OneToOneField(
        MalfunctionReport, on_delete=models.SET_DEFAULT, default=0
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_DEFAULT, default=0
    )
    datetime = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    image = models.ImageField(upload_to="media/service_reports", blank=True)
