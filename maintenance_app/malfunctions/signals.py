from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import MalfunctionReport, ServiceReport
from machines.models import Machine


@receiver(post_save, sender=MalfunctionReport)
def malfunction_change_machine_status(sender, created, instance, **kwargs):
    if created:
        machine = Machine.objects.get(pk=instance.machine.pk)
        machine.machine_status = "nonwork"
        machine.save()
