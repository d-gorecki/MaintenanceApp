from io import StringIO

from django.core import mail
from django.core.management import call_command
from django.test import TestCase
from django.utils.timezone import datetime, now, timedelta

from maintenance.tests.test_models import MaintenanceTestUtils


class TestSendRemainder(TestCase):
    def setUp(self):
        tomorrow = datetime.date(now()) + timedelta(1)
        self.schedule = MaintenanceTestUtils.create_maintenance_schedule(
            planned_date=tomorrow
        )

    def test_command_output(self):
        call_command("sendremainder", stdout=StringIO())
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(
            mail.outbox[0].subject,
            f"Reminder: Tomorrow maintenance of {self.schedule.machine.name}.",
        )
