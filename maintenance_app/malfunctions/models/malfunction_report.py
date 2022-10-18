from django.db import models
from machines.models.machine import Machine
from django.conf import settings


class MalfunctionsPendingManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status="pending")


class MalfunctionReport(models.Model):
    STATUS: tuple[tuple[str]] = (("pending", "pending"), ("finished", "finished"))

    machine = models.ForeignKey(Machine, on_delete=models.CASCADE, help_text="Machine")
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_DEFAULT,
        default=0,
        help_text="Reporting user",
    )
    datetime = models.DateTimeField(auto_now_add=True)
    description = models.TextField(help_text="Description")
    image = models.ImageField(
        upload_to="media/malfunction_issues",
        help_text="Allowed format (.jpg, .png)",
        blank=True,
    )
    status = models.CharField(
        max_length=8, choices=STATUS, default="pending", help_text="Machine status"
    )

    objects = models.Manager()
    pending = MalfunctionsPendingManager()

    def __str__(self):
        return f"#{self.pk}-{self.machine}"
