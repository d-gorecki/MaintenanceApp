from django.core.management.base import BaseCommand
from departments.models import Department
from machines.models.machine_group import MachineGroup


class Command(BaseCommand):
    """Management command to create initial Department and MachineGroup models for presentation purposes during the first run of the app"""

    def handle(self, *args, **options) -> None:
        if not Department.objects.count():
            Department.objects.create(name="Example_department")
        if not MachineGroup.objects.count():
            MachineGroup.objects.create(name="Example_machine_group")
