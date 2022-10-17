from django.test import TestCase
from malfunctions.models.malfunction_report import MalfunctionReport
from malfunctions.models.service_report import ServiceReport
from departments.models import Department
from users.models import User
from machines.models.machine_group import MachineGroup
from machines.models.machine import Machine
from django.utils.timezone import now as django_now
from django.urls import reverse


class MalfunctionPendingViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        department_1 = Department.objects.create(name="Department1")
        department_2 = Department.objects.create(name="Department2")
        machine_group = MachineGroup.objects.create(name="Test")
        machine = Machine.objects.create(
            factory_number="11111",
            machine_group=machine_group,
            name="Test-name",
            number="1111",
            producer="test",
            purchase_data=django_now(),
            department=department_1,
            machine_status="available",
        )

        user_1 = User.objects.create_user(
            username="test1",
            password="zaq1@WSX",
            department=department_1,
            group="manager",
        )

        user_2 = User.objects.create_user(
            username="test2",
            password="zaq1@WSX",
            department=department_2,
            group="production",
        )

        User.objects.create_user(
            username="noprivilages",
            password="zaq1@WSX",
            department=department_2,
            group="production",
        )

        cls.malfunction_reports = [
            MalfunctionReport.objects.create(
                machine=machine, user=user_2, description="test", status="pending"
            )
            for _ in range(3)
        ]

    def test_url_exists_at_desired_location(self):
        self.client.login(username="test1", password="zaq1@WSX")
        response = self.client.get("/malfunctions/pending/")
        self.assertEqual(response.status_code, 200)

    def test_accessible_by_url_name(self):
        self.client.login(username="test1", password="zaq1@WSX")
        response = self.client.get((reverse("malfunctions_pending")))
        self.assertEqual(response.status_code, 200)

    def test_uses_correct_template(self):
        self.client.login(username="test1", password="zaq1@WSX")
        response = self.client.get((reverse("malfunctions_pending")))
        self.assertTemplateUsed(response, "malfunctions/malfunctions_pending.html")

    def test_redirect_if_not_logged_in(self):
        response = self.client.get((reverse("malfunctions_pending")))
        self.assertRedirects(response, "/users/login/?next=/malfunctions/pending/")

    def test_displays_proper_list_of_objects(self):
        self.client.login(username="test1", password="zaq1@WSX")
        response = self.client.get((reverse("malfunctions_pending")))
        self.assertEqual(len(response.context["malfunctions"]), 3)

    def test_403_if_not_manager(self):
        self.client.login(username="noprivilages", password="zaq1@WSX")
        response = self.client.get((reverse("malfunctions_pending")))
        self.assertEqual(response.status_code, 403)


class MalfunctionServicesBaseTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        department_1 = Department.objects.create(name="Department1")
        department_2 = Department.objects.create(name="Department2")
        machine_group = MachineGroup.objects.create(name="Test")
        machine = Machine.objects.create(
            factory_number="11111",
            machine_group=machine_group,
            name="Test-name",
            number="1111",
            producer="test",
            purchase_data=django_now(),
            department=department_1,
            machine_status="available",
        )

        user_1 = User.objects.create_user(
            username="test1",
            password="zaq1@WSX",
            department=department_1,
            group="manager",
        )

        user_2 = User.objects.create_user(
            username="test2",
            password="zaq1@WSX",
            department=department_2,
            group="production",
        )

        User.objects.create_user(
            username="noprivilages",
            password="zaq1@WSX",
            department=department_2,
            group="production",
        )

        malfunction_reports = [
            MalfunctionReport.objects.create(
                machine=machine, user=user_2, description="test", status="pending"
            )
            for _ in range(3)
        ]

        malfunction_services = [
            ServiceReport.objects.create(
                malfunction_report=malfunction_reports[i],
                user=user_2,
                description="test",
                service="finished",
            )
            for i in range(3)
        ]

    def test_url_exists_at_desired_location(self):
        self.client.login(username="test1", password="zaq1@WSX")
        response = self.client.get("/malfunctions/services/")
        self.assertEqual(response.status_code, 200)

    def test_accessible_by_url_name(self):
        self.client.login(username="test1", password="zaq1@WSX")
        response = self.client.get((reverse("malfunctions_services")))
        self.assertEqual(response.status_code, 200)

    def test_uses_correct_template(self):
        self.client.login(username="test1", password="zaq1@WSX")
        response = self.client.get((reverse("malfunctions_services")))
        self.assertTemplateUsed(response, "malfunctions/malfunctions_services.html")

    def test_redirect_if_not_logged_in(self):
        response = self.client.get((reverse("malfunctions_services")))
        self.assertRedirects(response, "/users/login/?next=/malfunctions/services/")

    def test_displays_proper_list_of_objects(self):
        self.client.login(username="test1", password="zaq1@WSX")
        response = self.client.get((reverse("malfunctions_services")))
        self.assertEqual(len(response.context["services"]), 3)

    def test_403_if_not_manager(self):
        self.client.login(username="noprivilages", password="zaq1@WSX")
        response = self.client.get((reverse("malfunctions_pending")))
        self.assertEqual(response.status_code, 403)
