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

    GROUP = (
        ("manager", "manager"),
        ("maintenance", "maintenance"),
        ("production", "production"),
    )

    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=70, blank=True)
    department = models.ForeignKey(
        Department, on_delete=models.SET_DEFAULT, default=1, blank=True
    )
    group = models.CharField(max_length=20, choices=GROUP, blank=True)
    email = models.EmailField(blank=True)
    function = models.CharField(max_length=50, choices=FUNCTION, blank=True)
    mobile = models.CharField(max_length=12, blank=True)

    def is_manager(self):
        return self.group.filter(name="manager").exists()

    def is_maintenance(self):
        return self.group.filter(name="maintenance").exists()

    def is_production(self):
        return self.group.filter(name="production").exists()
