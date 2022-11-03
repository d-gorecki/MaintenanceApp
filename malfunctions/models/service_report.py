from django.db import models
from django.conf import settings
from malfunctions.models.malfunction_report import MalfunctionReport


class ServicesDashboardManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().order_by("-id")[:3]


class ServiceReport(models.Model):
    STATUS: tuple[tuple[str]] = (
        ("pending", "pending"),
        ("finished", "finished"),
    )

    malfunction_report = models.ForeignKey(
        MalfunctionReport,
        on_delete=models.SET_DEFAULT,
        default=0,
        help_text="Corresponding malfunction report",
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_DEFAULT,
        default=0,
        help_text="Serviceman",
    )
    datetime = models.DateTimeField(auto_now_add=True)
    description = models.TextField(help_text="Description")
    image = models.ImageField(
        upload_to="media/service_reports",
        blank=True,
        help_text="Allowed formats (.png, .jpg)",
    )
    service = models.CharField(
        max_length=8,
        choices=STATUS,
        default="pending",
        help_text="Status after service",
    )

    objects = models.Manager()
    services_dashboard = ServicesDashboardManager()

    def save(self, *args, **kwargs) -> None:
        """If ServiceReport status field has been set to finished, save method sets status of corresponding
        MalfunctionReport to finished. Then method checks if there are any other MalfunctionReport objects with pending
        status for ServiceReport.machine. In case of empty queryset method sets ServiceReport.machine status
        to available."""
        super(ServiceReport, self).save(*args, **kwargs)

        if self.service == "finished":
            malfunction_report = MalfunctionReport.objects.get(
                pk=self.malfunction_report.pk
            )
            malfunction_report.status = "finished"
            malfunction_report.save()

        machine = MalfunctionReport.objects.get(pk=self.malfunction_report.pk).machine
        malfunction_report = MalfunctionReport.objects.filter(
            machine=machine, status="pending"
        )
        if not malfunction_report:
            machine.machine_status = "available"
            machine.save()
