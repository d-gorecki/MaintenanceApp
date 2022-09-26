from django.contrib.auth.models import User
from django.db import models
from machines.models import Machine


class MalfunctionReport(models.Model):
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default=0)
    datetime = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    image = models.ImageField(upload_to="media/malfunction_issues")
