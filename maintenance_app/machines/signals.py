from typing import Any

from django.db.models.signals import post_save
from django.dispatch import receiver
from malfunctions.models import MalfunctionReport
from .models import Machine


@receiver(post_save, sender=MalfunctionReport)
def change_machine_status(
    sender: MalfunctionReport,
    created: bool,
    instance: MalfunctionReport,
    **kwargs: dict[str, Any]
) -> None:
    machine: Machine = Machine.objects.get(pk=instance.machine.pk)
    machine.machine_status = "nonwork"
    machine.save()
