from django.test import TestCase
from maintenance.models.maintenance_report import MaintenanceReport
from maintenance.models.maintenance_schedule import MaintenanceSchedule
from maintenance.models.maintenance_type import MaintenanceType
from users.models import User
from machines.models.machine import Machine
from machines.models.machine_group import MachineGroup
from django.utils.timezone import now as django_now
from departments.models import Department


class MaintenanceTypeTest(TestCase):
    @classmethod
    def setUp(cls):
        machine_group = MachineGroup.objects.create(name="Test")
        cls.machine_group_id = machine_group.pk
        cls.maintenance_id = MaintenanceType.objects.create(
            type="week", description="Test", machine_group=machine_group
        ).pk

    def test_type_label(self):
        maintenance_type = MaintenanceType.objects.get(pk=self.maintenance_id)
        field_label = maintenance_type._meta.get_field("type").verbose_name
        self.assertEqual(field_label, "type")

    def test_type_max_length(self):
        maintenance_type = MaintenanceType.objects.get(pk=self.maintenance_id)
        max_length = maintenance_type._meta.get_field("type").max_length
        self.assertEqual(max_length, 50)

    def test_description_label(self):
        maintenance_type = MaintenanceType.objects.get(pk=self.maintenance_id)
        field_label = maintenance_type._meta.get_field("type").verbose_name
        self.assertEqual(field_label, "type")

    def test_machine_group_label(self):
        maintenance_type = MaintenanceType.objects.get(pk=self.maintenance_id)
        field_label = maintenance_type._meta.get_field("machine_group").verbose_name
        self.assertEqual(field_label, "machine group")

    def test_obj_str_method_is_type_group(self):
        maintenance_type = MaintenanceType.objects.get(pk=self.maintenance_id)
        expected_obj_str = f"{maintenance_type.type}: {maintenance_type.machine_group}"
        self.assertEqual(str(maintenance_type), expected_obj_str)


class MaintenanceScheduleTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.department_id = Department.objects.create(name="Test").pk

        cls.machine_group_id = MachineGroup.objects.create(name="Test-group").pk

        cls.machine_id = Machine.objects.create(
            name="Test machine",
            machine_group=MachineGroup.objects.get(pk=cls.machine_group_id),
            department=Department.objects.get(pk=cls.department_id),
        ).pk

        cls.user_id = User.objects.create(
            username="TestUser", department=Department.objects.get(pk=cls.department_id)
        ).pk

        cls.maintenance_type_id = MaintenanceType.objects.create(
            type="week", machine_group=MachineGroup.objects.get(pk=cls.machine_group_id)
        ).pk

        cls.obj_id = MaintenanceSchedule.objects.create(
            machine=Machine.objects.get(pk=cls.machine_id),
            maintenance_type=MaintenanceType.objects.get(pk=cls.maintenance_type_id),
            user=User.objects.get(pk=cls.user_id),
            planned_date=django_now(),
        ).pk

    def test_machine_label(self):
        schedule = MaintenanceSchedule.objects.get(pk=self.obj_id)
        field_label = schedule._meta.get_field("machine").verbose_name
        self.assertEqual(field_label, "machine")

    def test_maintenance_type_label(self):
        schedule = MaintenanceSchedule.objects.get(pk=self.obj_id)
        field_label = schedule._meta.get_field("maintenance_type").verbose_name
        self.assertEqual(field_label, "maintenance type")

    def test_planned_date_label(self):
        schedule = MaintenanceSchedule.objects.get(pk=self.obj_id)
        field_label = schedule._meta.get_field("planned_date").verbose_name
        self.assertEqual(field_label, "planned date")

    def test_user_type_label(self):
        schedule = MaintenanceSchedule.objects.get(pk=self.obj_id)
        field_label = schedule._meta.get_field("user").verbose_name
        self.assertEqual(field_label, "user")

    def test_status_type_label(self):
        schedule = MaintenanceSchedule.objects.get(pk=self.obj_id)
        field_label = schedule._meta.get_field("status").verbose_name
        self.assertEqual(field_label, "status")

    def test_obj_str_method_is_type_group(self):
        schedule = MaintenanceSchedule.objects.get(pk=self.obj_id)
        expected_obj_str = f"{schedule.maintenance_type}: {schedule.planned_date}"
        self.assertEqual(str(schedule), expected_obj_str)


class MaintenanceReportTest(TestCase):
    @classmethod
    def setUp(cls):
        cls.department_id = Department.objects.create(name="Test").pk

        cls.machine_group_id = MachineGroup.objects.create(name="Test-group").pk

        cls.machine_id = Machine.objects.create(
            name="Test machine",
            machine_group=MachineGroup.objects.get(pk=cls.machine_group_id),
            department=Department.objects.get(pk=cls.department_id),
        ).pk

        cls.user_id = User.objects.create(
            username="TestUser", department=Department.objects.get(pk=cls.department_id)
        ).pk

        cls.maintenance_type_id = MaintenanceType.objects.create(
            type="week", machine_group=MachineGroup.objects.get(pk=cls.machine_group_id)
        ).pk

        cls.schedule_id = MaintenanceSchedule.objects.create(
            machine=Machine.objects.get(pk=cls.machine_id),
            maintenance_type=MaintenanceType.objects.get(pk=cls.maintenance_type_id),
            user=User.objects.get(pk=cls.user_id),
            planned_date=django_now(),
        ).pk

        cls.obj_id = MaintenanceReport.objects.create(
            date=django_now(),
            schedule=MaintenanceSchedule.objects.get(pk=cls.schedule_id),
            user=User.objects.get(pk=cls.user_id),
            description="Test123",
        ).pk

    def test_date_label(self):
        report = MaintenanceReport.objects.get(id=self.obj_id)
        field_label = report._meta.get_field("date").verbose_name
        self.assertEqual(field_label, "date")

    def test_schedule_label(self):
        report = MaintenanceReport.objects.get(id=self.obj_id)
        field_label = report._meta.get_field("schedule").verbose_name
        self.assertEqual(field_label, "schedule")

    def test_user_label(self):
        report = MaintenanceReport.objects.get(id=self.obj_id)
        field_label = report._meta.get_field("user").verbose_name
        self.assertEqual(field_label, "user")

    def test_description_label(self):
        report = MaintenanceReport.objects.get(id=self.obj_id)
        field_label = report._meta.get_field("description").verbose_name
        self.assertEqual(field_label, "description")

    def test_image_label(self):
        report = MaintenanceReport.objects.get(id=self.obj_id)
        field_label = report._meta.get_field("image").verbose_name
        self.assertEqual(field_label, "image")
