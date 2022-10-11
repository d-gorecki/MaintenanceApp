from django.db import models
from django.conf import settings
from PIL import Image
from maintenance.models.maintenance_schedule import MaintenanceSchedule


class MaintenanceReport(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    schedule = models.OneToOneField(
        MaintenanceSchedule,
        on_delete=models.SET_NULL,
        null=True,
        help_text="Corresponding maintenance schedule",
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        help_text="Serviceman",
    )
    description = models.TextField(help_text="Description")
    image = models.ImageField(
        upload_to="media/maintenance_reports",
        help_text="Allowed formats (.jpg, .png)",
        blank=True,
    )

    def save(self, *args, **kwargs) -> None:
        """Resize passed images with resolution higher than 800x800 before saving to database"""
        super().save(*args, **kwargs)
        if self.image:
            img: Image = Image.open(self.image.path)

            if img.height > 800 or img.width > 800:
                output_size: tuple[int] = (800, 800)
                img.thumbnail(output_size)
                img.save(self.image.path)
