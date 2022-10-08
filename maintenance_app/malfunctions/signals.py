from django.db.models.signals import post_save
from django.dispatch import receiver
from malfunctions.models import MalfunctionReport
from .models import Machine


@receiver(post_save, sender=MalfunctionReport)
def change_machine_status(sender, created, instance, **kwargs):
    machine = Machine.objects.get(pk=instance.machine.pk)
    machine.machine_status = "nonwork"
    machine.save()
