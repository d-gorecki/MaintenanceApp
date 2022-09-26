from django.contrib.auth.models import User
from django.db import models
from machines.models import Machine


class MalfunctionReport(models.Model):
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default=0)
    datetime = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    image = models.ImageField(upload_to="media/malfunction_issues")


class MalfunctionPending(models.Model):
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE)
    malfunction_report = models.OneToOneField(
        MalfunctionReport, on_delete=models.CASCADE
    )

    # prop unnecessary model


class ServiceReport(models.Model):
    machine = models.ForeignKey(Machine, on_delete=models.SET_DEFAULT, default=0)
    malfunction_report = models.OneToOneField(
        MalfunctionReport, on_delete=models.SET_DEFAULT, default=0
    )
    user = models.OneToOneField(User, on_delete=models.SET_DEFAULT, default=0)
    datetime = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    image = models.ImageField(upload_to="media/malfunction_reports")
