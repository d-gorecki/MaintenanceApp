from typing import Any
from django.db.models.signals import post_save
from django.dispatch import receiver
from maintenance.models.maintenance_report import MaintenanceReport
from maintenance.models.maintenance_schedule import MaintenanceSchedule


@receiver(post_save, sender=MaintenanceReport)
def change_maintenance_schedule_status(
    sender: MaintenanceReport,
    created: bool,
    instance: MaintenanceReport,
    **kwargs: dict[str, Any]
) -> None:
    maintenance_schedule: MaintenanceSchedule = MaintenanceSchedule.objects.get(
        pk=instance.schedule.pk
    )
    maintenance_schedule.status = "done"
    maintenance_schedule.save()
