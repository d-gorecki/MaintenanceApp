from io import StringIO
from django.core.management import call_command
from django.test import TestCase
from maintenance.models.maintenance_schedule import MaintenanceSchedule
from maintenance.models.maintenance_type import MaintenanceType
from machines.models.machine_group import MachineGroup
from machines.models.machine import Machine
from departments.models import Department
from django.utils.timezone import datetime, now, timedelta
from users.models import User
from django.core import mail


class SendRemainderTest(TestCase):
    def setUp(self):
        tomorrow = datetime.date(now()) + timedelta(1)
        machine_group = MachineGroup.objects.create(name="test")
        maintenance_type = MaintenanceType.objects.create(
            type="week", description="test", machine_group=machine_group
        )
        department = Department.objects.create(name="test")
        machine = Machine.objects.create(
            factory_number="1", machine_group=machine_group, department=department
        )
        user = User.objects.create_user(
            username="test1",
            first_name="Test",
            last_name="Test",
            password="zaq1@WSX",
            department=department,
            group="manager",
            email="testemail@gmail.com",
        )
        self.schedule = MaintenanceSchedule.objects.create(
            machine=machine,
            maintenance_type=maintenance_type,
            planned_date=tomorrow,
            user=user,
            status="pending",
        )

    def test_command_output(self):
        call_command("sendremainder", stdout=StringIO())
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(
            mail.outbox[0].subject,
            f"Reminder: Tomorrow maintenance of {self.schedule.machine.name}.",
        )
