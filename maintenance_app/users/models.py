from django.db import models
from django.contrib.auth.models import AbstractUser, User
from departments.models import Department


class User(AbstractUser):
    FUNCTION = (
        ("electrican", "electrican"),
        ("mechanic", "mechanic"),
        ("automation_serviceman", "automation serviceman"),
        ("maintenance_supervisor", "maintenance supervisor"),
        ("department_supervisor", "department supervisor"),
        ("production_worker", "production worker"),
    )

    GROUP = (("report", "report"), ("view", "view"), ("manage", "manage"))

    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=70, blank=True)
    department = models.ForeignKey(
        Department, on_delete=models.SET_DEFAULT, default=1, blank=True
    )
    group = models.CharField(max_length=20, choices=GROUP, blank=True)
    email = models.EmailField(blank=True)
    function = models.CharField(max_length=50, choices=FUNCTION, blank=True)
    mobile = models.CharField(max_length=12, blank=True)
