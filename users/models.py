from django.db import models
from django.contrib.auth.models import AbstractUser
from departments.models import Department


class User(AbstractUser):
    FUNCTION: tuple[tuple[str]] = (
        ("electrican", "electrican"),
        ("mechanic", "mechanic"),
        ("automation_serviceman", "automation serviceman"),
        ("maintenance_supervisor", "maintenance supervisor"),
        ("department_supervisor", "department supervisor"),
        ("production_worker", "production worker"),
    )

    GROUP: tuple[tuple[str]] = (
        ("manager", "manager"),
        ("maintenance", "maintenance"),
        ("production", "production"),
    )

    first_name = models.CharField(max_length=50, blank=True, help_text="First name")
    last_name = models.CharField(max_length=70, blank=True, help_text="Last name")
    department = models.ForeignKey(
        Department,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        help_text="Department",
    )
    group = models.CharField(
        max_length=20, choices=GROUP, blank=True, help_text="Privileges group"
    )
    email = models.EmailField(blank=True, help_text="Email")
    function = models.CharField(
        max_length=50, choices=FUNCTION, blank=True, help_text="Function"
    )
    mobile = models.CharField(max_length=12, blank=True, help_text="Mobile")
