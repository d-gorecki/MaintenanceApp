from django.db import models
from machines.models import MachineGroup, Machine
from django.contrib.auth.models import User
from django.conf import settings
from PIL import Image

# TODO help_text
class MaintenanceType(models.Model):
    MAINTENANCE_TYPES = (
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


class MaintenanceSchedule(models.Model):
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE, help_text="Machine")
    maintenance_type = models.ForeignKey(
        MaintenanceType, on_delete=models.CASCADE, help_text="Maintenance type"
    )
    planned_date = models.DateField(help_text="Maintenance planned date")
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_DEFAULT,
        default=0,
        help_text="Responsible",
    )
    # on user deletion app should reassign another user to planned maintenance

    def __str__(self):
        return f"{self.maintenance_type}: {self.planned_date}"


class MaintenanceReport(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    schedule = models.ForeignKey(
        MaintenanceSchedule,
        on_delete=models.SET_DEFAULT,
        default=1,
        help_text="Corresponding maintenance schedule",
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_DEFAULT,
        default=3,
        help_text="Serviceman",
    )
    description = models.TextField(help_text="Description")
    image = models.ImageField(
        upload_to="media/maintenance_reports", help_text="Allowed formats (.jpg, .png)"
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # TODO Refactor to use django signal instaed of override .save() method
        img = Image.open(self.image.path)

        if img.height > 800 or img.width > 800:
            output_size = (800, 800)
            img.thumbnail(output_size)
            img.save(self.image.path)
