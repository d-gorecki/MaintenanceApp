from django.test import TestCase
from django.utils.timezone import now as django_now

from dashboard.tests import UserTestUtils
from machines.models.machine_group import MachineGroup
from machines.tests.test_models import MachineTestUtils
from maintenance.models.maintenance_report import MaintenanceReport
from maintenance.models.maintenance_schedule import MaintenanceSchedule
from maintenance.models.maintenance_type import MaintenanceType


class MaintenanceTestUtils:
    @staticmethod
    def create_maintenance_type(type="week", description="Test", machine_group=None):
        if not machine_group:
            machine_group = MachineGroup.objects.create(name="Test")
        return MaintenanceType.objects.create(
            type=type, description=description, machine_group=machine_group
        )

    @staticmethod
    def create_maintenance_schedule(
        machine=None,
        maintenance_type=None,
        user=None,
        planned_date=None,
        status="pending",
    ):
        machine_group = MachineGroup.objects.create(name="group1")
        if not machine:
            machine = MachineTestUtils.create_machine(machine_group=machine_group)
        if not maintenance_type:
            maintenance_type = MaintenanceTestUtils.create_maintenance_type(
                machine_group=machine_group
            )
        if not user:
            user = UserTestUtils.create_user()
        if not planned_date:
            planned_date = django_now()

        return MaintenanceSchedule.objects.create(
            machine=machine,
            maintenance_type=maintenance_type,
            planned_date=planned_date,
            user=user,
            status=status,
        )

    @staticmethod
    def create_maintenance_report(
        date=None, schedule=None, user=None, description="Test"
    ):
        if not date:
            date = django_now()
        if not user:
            user = UserTestUtils.create_user()
        if not schedule:
            schedule = MaintenanceTestUtils.create_maintenance_schedule(user=user)

        return MaintenanceReport.objects.create(
            date=date, user=user, schedule=schedule, description=description
        )


class TestMaintenanceType(TestCase):
    @classmethod
    def setUp(cls):
        cls.maintenance = MaintenanceTestUtils.create_maintenance_type()

    def test_type_label(self):
        maintenance_type = self.maintenance
        field_label = maintenance_type._meta.get_field("type").verbose_name
        self.assertEqual(field_label, "type")

    def test_type_max_length(self):
        maintenance_type = self.maintenance
        max_length = maintenance_type._meta.get_field("type").max_length
        self.assertEqual(max_length, 50)

    def test_description_label(self):
        maintenance_type = self.maintenance
        field_label = maintenance_type._meta.get_field("type").verbose_name
        self.assertEqual(field_label, "type")

    def test_machine_group_label(self):
        maintenance_type = self.maintenance
        field_label = maintenance_type._meta.get_field("machine_group").verbose_name
        self.assertEqual(field_label, "machine group")

    def test_obj_str_method_is_type_group(self):
        maintenance_type = self.maintenance
        expected_obj_str = f"{maintenance_type.type}: {maintenance_type.machine_group}"
        self.assertEqual(str(maintenance_type), expected_obj_str)


class TestMaintenanceSchedule(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.maintenance_schedule = MaintenanceTestUtils.create_maintenance_schedule()

    def test_machine_label(self):
        schedule = self.maintenance_schedule
        field_label = schedule._meta.get_field("machine").verbose_name
        self.assertEqual(field_label, "machine")

    def test_maintenance_type_label(self):
        schedule = self.maintenance_schedule
        field_label = schedule._meta.get_field("maintenance_type").verbose_name
        self.assertEqual(field_label, "maintenance type")

    def test_planned_date_label(self):
        schedule = self.maintenance_schedule
        field_label = schedule._meta.get_field("planned_date").verbose_name
        self.assertEqual(field_label, "planned date")

    def test_user_type_label(self):
        schedule = self.maintenance_schedule
        field_label = schedule._meta.get_field("user").verbose_name
        self.assertEqual(field_label, "user")

    def test_status_type_label(self):
        schedule = self.maintenance_schedule
        field_label = schedule._meta.get_field("status").verbose_name
        self.assertEqual(field_label, "status")

    def test_obj_str_method_is_type_group(self):
        schedule = self.maintenance_schedule
        expected_obj_str = f"{schedule.maintenance_type}: {schedule.planned_date}"
        self.assertEqual(str(schedule), expected_obj_str)


class TestMaintenanceReport(TestCase):
    @classmethod
    def setUp(cls):
        cls.maintenance_report = MaintenanceTestUtils.create_maintenance_report()

    def test_date_label(self):
        report = self.maintenance_report
        field_label = report._meta.get_field("date").verbose_name
        self.assertEqual(field_label, "date")

    def test_schedule_label(self):
        report = self.maintenance_report
        field_label = report._meta.get_field("schedule").verbose_name
        self.assertEqual(field_label, "schedule")

    def test_user_label(self):
        report = self.maintenance_report
        field_label = report._meta.get_field("user").verbose_name
        self.assertEqual(field_label, "user")

    def test_description_label(self):
        report = self.maintenance_report
        field_label = report._meta.get_field("description").verbose_name
        self.assertEqual(field_label, "description")

    def test_image_label(self):
        report = self.maintenance_report
        field_label = report._meta.get_field("image").verbose_name
        self.assertEqual(field_label, "image")
