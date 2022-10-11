import pytest
from .models import MaintenanceType, MaintenanceSchedule, MaintenanceReport
from machines.models import MachineGroup, Machine


@pytest.mark.django_db
def test_maintenance_type_create():
    machine_group = MachineGroup.objects.create(name="test_group")
    MaintenanceType.objects.create(machine_group=machine_group)
    MaintenanceType.objects.count() == 1


@pytest.mark.django_db
def test_maintenance_schedule_create():
    maintenance_type = MaintenanceType


def test_maintenance_report_create():
    pass
