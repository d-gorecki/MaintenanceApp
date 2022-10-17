from django.test import TestCase
from malfunctions.forms.report_form import ReportForm
from malfunctions.forms.service_report_form import ServiceReportForm
from malfunctions.models.malfunction_report import MalfunctionReport
from machines.models.machine import Machine
from machines.models.machine_group import MachineGroup
from departments.models import Department
from users.models import User
from django.utils.timezone import now as django_now


class MalfunctionFormsTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        machine_group = MachineGroup.objects.create(name="test")
        department = Department.objects.create(name="test")
        machine = Machine.objects.create(
            name="Test machine",
            machine_group=machine_group,
            department=department,
        )
        cls.user = User.objects.create(username="Test", department=department)
        MalfunctionReport.objects.create(
            machine=machine,
            user=cls.user,
            datetime=django_now(),
            description="Test",
            status="pending",
        )

    def test_report_form(self):
        form = ReportForm(user=self.user)
        fields = ["machine", "description", "image"]
        for field in fields:
            self.assertIn(field, form.fields)

    def test_service_report(self):
        form = ServiceReportForm()
        fields = ["malfunction_report", "description", "image", "service"]
        for field in fields:
            self.assertIn(field, form.fields)
