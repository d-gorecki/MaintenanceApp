import pytest
from machines.models.machine import Machine
from machines.models.machine_group import MachineGroup

from departments.models import Department


@pytest.mark.django_db
def test_machine_create():
    machine_group = MachineGroup.objects.create(name="test_machine_group")
    department = Department.objects.create(name="test_department")
    Machine.objects.create(machine_group=machine_group, department=department)
    assert Machine.objects.count() == 1
