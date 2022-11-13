from django.test import TestCase
from django.utils.timezone import now as django_now

from dashboard.tests import UserTestUtils
from machines.tests.test_models import MachineTestUtils
from malfunctions.models.malfunction_report import MalfunctionReport
from malfunctions.models.service_report import ServiceReport


class MalfunctionTestUtils:
    @staticmethod
    def create_malfunction_report(
        machine=None, user=None, datetime=None, description="Test", status="pending"
    ):
        if not machine:
            machine = MachineTestUtils.create_machine()
        if not user:
            user = UserTestUtils.create_user()
        if not datetime:
            datetime = django_now()

        return MalfunctionReport.objects.create(
            machine=machine,
            user=user,
            datetime=datetime,
            description=description,
            status=status,
        )

    @staticmethod
    def create_service_report(
        malfunction_report=None,
        user=None,
        datetime=None,
        description="Test",
        service="pending",
    ):
        if not user:
            user = UserTestUtils.create_user()
        if not malfunction_report:
            malfunction_report = MalfunctionTestUtils.create_malfunction_report(
                user=user
            )
        if not datetime:
            datetime = django_now()

        return ServiceReport.objects.create(
            malfunction_report=malfunction_report,
            user=user,
            datetime=datetime,
            description=description,
            service=service,
        )


class TestMalfunctionReport(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.malfunction_report = MalfunctionTestUtils.create_malfunction_report()

    def test_machine_label(self):
        malfunction = self.malfunction_report
        field_label = malfunction._meta.get_field("machine").verbose_name
        self.assertEqual(field_label, "machine")

    def test_user_label(self):
        malfunction = self.malfunction_report
        field_label = malfunction._meta.get_field("user").verbose_name
        self.assertEqual(field_label, "user")

    def test_datetime_label(self):
        malfunction = self.malfunction_report
        field_label = malfunction._meta.get_field("datetime").verbose_name
        self.assertEqual(field_label, "datetime")

    def test_description_label(self):
        malfunction = self.malfunction_report
        field_label = malfunction._meta.get_field("description").verbose_name
        self.assertEqual(field_label, "description")

    def test_image_label(self):
        malfunction = self.malfunction_report
        field_label = malfunction._meta.get_field("image").verbose_name
        self.assertEqual(field_label, "image")

    def test_status_label(self):
        malfunction = self.malfunction_report
        field_label = malfunction._meta.get_field("status").verbose_name
        self.assertEqual(field_label, "status")

    def test_status_max_length(self):
        malfunction = self.malfunction_report
        max_length = malfunction._meta.get_field("status").max_length
        self.assertEqual(max_length, 8)

    def test_obj_str_method_is_pk_machine(self):
        malfunction = self.malfunction_report
        expected_obj_str = f"#{malfunction.pk}-{malfunction.machine}"
        self.assertEqual(str(malfunction), expected_obj_str)


class TestServiceReport(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.service_report = MalfunctionTestUtils.create_service_report()

    def test_malfunction_report_label(self):
        service = self.service_report
        field_label = service._meta.get_field("malfunction_report").verbose_name
        self.assertEqual(field_label, "malfunction report")

    def test_user_label(self):
        service = self.service_report
        field_label = service._meta.get_field("user").verbose_name
        self.assertEqual(field_label, "user")

    def test_datetime_label(self):
        service = self.service_report
        field_label = service._meta.get_field("datetime").verbose_name
        self.assertEqual(field_label, "datetime")

    def test_description_label(self):
        service = self.service_report
        field_label = service._meta.get_field("description").verbose_name
        self.assertEqual(field_label, "description")

    def test_image_label(self):
        service = self.service_report
        field_label = service._meta.get_field("image").verbose_name
        self.assertEqual(field_label, "image")

    def test_service_label(self):
        service = self.service_report
        field_label = service._meta.get_field("service").verbose_name
        self.assertEqual(field_label, "service")

    def test_service_max_length(self):
        service = self.service_report
        max_length = service._meta.get_field("service").max_length
        self.assertEqual(max_length, 8)
