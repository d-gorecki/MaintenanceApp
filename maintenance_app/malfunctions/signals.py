from typing import Any

from django.db.models.signals import post_save
from django.dispatch import receiver
from malfunctions.models.malfunction_report import MalfunctionReport
from machines.models.machine import Machine


@receiver(post_save, sender=MalfunctionReport)
def malfunction_change_machine_status(
    sender: MalfunctionReport,
    created: bool,
    instance: MalfunctionReport,
    **kwargs: dict[str, Any]
) -> None:
    if created:
        machine: Machine = Machine.objects.get(pk=instance.machine.pk)
        machine.machine_status = "nonwork"
        machine.save()
