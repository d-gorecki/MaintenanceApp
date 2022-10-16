from django.test import TestCase
from machines.models.machine_group import MachineGroup
from machines.models.machine import Machine
from departments.models import Department
from malfunctions.models.malfunction_report import MalfunctionReport
from malfunctions.models.service_report import ServiceReport
from users.models import User
from django.utils.timezone import now as django_now


class MalfunctionTestBaseClass(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.machine_group = MachineGroup.objects.create(name="test")
        cls.department = Department.objects.create(name="test")
        cls.machine = Machine.objects.create(
            name="Test machine",
            machine_group=cls.machine_group,
            department=cls.department,
        )
        cls.user = User.objects.create(username="Test", department=cls.department)
        cls.malfunction_report = MalfunctionReport.objects.create(
            machine=cls.machine,
            user=cls.user,
            datetime=django_now(),
            description="Test",
            status="pending",
        )


class MalfunctionReportTest(MalfunctionTestBaseClass):
    @classmethod
    def setUpTestData(cls):
        super(MalfunctionReportTest, cls).setUpTestData()
        cls.obj_id = cls.malfunction_report.pk

    def test_machine_label(self):
        malfunction = MalfunctionReport.objects.get(pk=self.obj_id)
        field_label = malfunction._meta.get_field("machine").verbose_name
        self.assertEqual(field_label, "machine")

    def test_user_label(self):
        malfunction = MalfunctionReport.objects.get(pk=self.obj_id)
        field_label = malfunction._meta.get_field("user").verbose_name
        self.assertEqual(field_label, "user")

    def test_datetime_label(self):
        malfunction = MalfunctionReport.objects.get(pk=self.obj_id)
        field_label = malfunction._meta.get_field("datetime").verbose_name
        self.assertEqual(field_label, "datetime")

    def test_description_label(self):
        malfunction = MalfunctionReport.objects.get(pk=self.obj_id)
        field_label = malfunction._meta.get_field("description").verbose_name
        self.assertEqual(field_label, "description")

    def test_image_label(self):
        malfunction = MalfunctionReport.objects.get(pk=self.obj_id)
        field_label = malfunction._meta.get_field("image").verbose_name
        self.assertEqual(field_label, "image")

    def test_status_label(self):
        malfunction = MalfunctionReport.objects.get(pk=self.obj_id)
        field_label = malfunction._meta.get_field("status").verbose_name
        self.assertEqual(field_label, "status")

    def test_status_max_length(self):
        malfunction = MalfunctionReport.objects.get(pk=self.obj_id)
        max_length = malfunction._meta.get_field("status").max_length
        self.assertEqual(max_length, 8)

    def test_obj_str_method_is_pk_machine(self):
        malfunction = MalfunctionReport.objects.get(pk=self.obj_id)
        expected_obj_str = f"#{malfunction.pk}-{malfunction.machine}"
        self.assertEqual(str(malfunction), expected_obj_str)


class ServiceReportTest(MalfunctionTestBaseClass):
    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()
        cls.obj_id = ServiceReport.objects.create(
            malfunction_report=cls.malfunction_report,
            user=cls.user,
            datetime=django_now(),
            description="test",
            service="pending",
        ).pk

    def test_malfunction_report_label(self):
        service = ServiceReport.objects.get(pk=self.obj_id)
        field_label = service._meta.get_field("malfunction_report").verbose_name
        self.assertEqual(field_label, "malfunction report")

    def test_user_label(self):
        service = ServiceReport.objects.get(pk=self.obj_id)
        field_label = service._meta.get_field("user").verbose_name
        self.assertEqual(field_label, "user")

    def test_datetime_label(self):
        service = ServiceReport.objects.get(pk=self.obj_id)
        field_label = service._meta.get_field("datetime").verbose_name
        self.assertEqual(field_label, "datetime")

    def test_description_label(self):
        service = ServiceReport.objects.get(pk=self.obj_id)
        field_label = service._meta.get_field("description").verbose_name
        self.assertEqual(field_label, "description")

    def test_image_label(self):
        service = ServiceReport.objects.get(pk=self.obj_id)
        field_label = service._meta.get_field("image").verbose_name
        self.assertEqual(field_label, "image")

    def test_service_label(self):
        service = ServiceReport.objects.get(pk=self.obj_id)
        field_label = service._meta.get_field("service").verbose_name
        self.assertEqual(field_label, "service")

    def test_service_max_length(self):
        service = ServiceReport.objects.get(pk=self.obj_id)
        max_length = service._meta.get_field("service").max_length
        self.assertEqual(max_length, 8)

    def test_service_report_sets_malfunction_report_status_as_finished(self):
        service = ServiceReport.objects.get(pk=self.obj_id)
        service.status = "finished"
        service.save()

        self.assertTrue(self.malfunction_report.status == "finished")
