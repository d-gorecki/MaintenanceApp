from django.test import TestCase
from django.urls import reverse
from departments.models import Department
from users.models import User
from maintenance.models.maintenance_report import MaintenanceReport
from maintenance.models.maintenance_schedule import MaintenanceSchedule
from maintenance.models.maintenance_type import MaintenanceType
from machines.models.machine_group import MachineGroup
from machines.models.machine import Machine
from django.utils.timezone import now as django_now
from django.utils.timezone import timedelta


class MaintenanceReportsBaseViewTest(TestCase):
    def setUp(self):
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

        maintenance_type = MaintenanceType.objects.create(
            type="week", description="test", machine_group=machine_group
        )

        schedules = [
            MaintenanceSchedule.objects.create(
                machine=machine,
                maintenance_type=maintenance_type,
                planned_date=django_now() + timedelta(i),
                user=user_1,
                status="pending",
            )
            for i in range(5)
        ]

        reports = [
            MaintenanceReport.objects.create(
                schedule=schedules[i], user=user_1, description="aaa"
            )
            for i in range(3)
        ]

    def test_url_exists_at_desired_location(self):
        self.client.login(username="test1", password="zaq1@WSX")
        response = self.client.get("/maintenance/schedules/reports/")
        self.assertEqual(response.status_code, 200)

    def test_accessible_by_url_name(self):
        self.client.login(username="test1", password="zaq1@WSX")
        response = self.client.get((reverse("maintenance_reports")))
        self.assertEqual(response.status_code, 200)

    def test_uses_correct_template(self):
        self.client.login(username="test1", password="zaq1@WSX")
        response = self.client.get((reverse("maintenance_reports")))
        self.assertTemplateUsed(response, "maintenance/maintenance_reports.html")

    def test_redirect_if_not_logged_in(self):
        response = self.client.get((reverse("maintenance_reports")))
        self.assertRedirects(
            response, "/users/login/?next=/maintenance/schedules/reports/"
        )

    def test_displays_proper_list_of_objects(self):
        self.client.login(username="test1", password="zaq1@WSX")
        response = self.client.get((reverse("maintenance_reports")))
        self.assertEqual(len(response.context["reports"]), 3)

    def test_403_if_not_manager(self):
        self.client.login(username="noprivilages", password="zaq1@WSX")
        response = self.client.get((reverse("maintenance_reports")))
        self.assertEqual(response.status_code, 403)


class MaintenanceReportsCreateViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        department_1 = Department.objects.create(name="Department1")
        department_2 = Department.objects.create(name="Department2")

        User.objects.create_user(
            username="test1",
            password="zaq1@WSX",
            department=department_1,
            group="manager",
        )

        User.objects.create_user(
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

    def test_url_exists_at_desired_location(self):
        self.client.login(username="test1", password="zaq1@WSX")
        response = self.client.get("/maintenance/schedules/reports/add")
        self.assertEqual(response.status_code, 200)

    def test_accessible_by_url_name(self):
        self.client.login(username="test1", password="zaq1@WSX")
        response = self.client.get((reverse("maintenance_reports_add")))
        self.assertEqual(response.status_code, 200)

    def test_uses_correct_template(self):
        self.client.login(username="test1", password="zaq1@WSX")
        response = self.client.get((reverse("maintenance_reports_add")))
        self.assertTemplateUsed(response, "maintenance/maintenance_reports_add.html")

    def test_redirect_if_not_logged_in(self):
        response = self.client.get((reverse("maintenance_reports_add")))
        self.assertRedirects(
            response, "/users/login/?next=/maintenance/schedules/reports/add"
        )

    def test_403_if_not_manager(self):
        self.client.login(username="noprivilages", password="zaq1@WSX")
        response = self.client.get((reverse("maintenance_reports_add")))
        self.assertEqual(response.status_code, 403)


class MaintenanceReportsDetailViewTest(TestCase):
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
            group="maintenance",
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

        maintenance_type = MaintenanceType.objects.create(
            type="week", description="test", machine_group=machine_group
        )

        schedule = MaintenanceSchedule.objects.create(
            machine=machine,
            maintenance_type=maintenance_type,
            planned_date=django_now(),
            user=user_1,
            status="pending",
        )

        cls.reports = MaintenanceReport.objects.create(
            schedule=schedule, user=user_1, description="aaa"
        )

    def test_url_exists_at_desired_location(self):
        self.client.login(username="test1", password="zaq1@WSX")
        response = self.client.get(f"/maintenance/schedules/reports/{self.reports.pk}")
        self.assertEqual(response.status_code, 200)

    def test_accessible_by_url_name(self):
        self.client.login(username="test1", password="zaq1@WSX")
        response = self.client.get(
            (reverse("maintenance_reports_detail", kwargs={"pk": self.reports.pk}))
        )
        self.assertEqual(response.status_code, 200)

    def test_uses_correct_template(self):
        self.client.login(username="test1", password="zaq1@WSX")
        response = self.client.get(
            (reverse("maintenance_reports_detail", kwargs={"pk": self.reports.pk}))
        )
        self.assertTemplateUsed(response, "maintenance/maintenance_reports_detail.html")

    def test_redirect_if_not_logged_in(self):
        response = self.client.get(
            (reverse("maintenance_reports_detail", kwargs={"pk": self.reports.pk}))
        )
        self.assertRedirects(
            response,
            f"/users/login/?next=/maintenance/schedules/reports/{self.reports.pk}",
        )

    def test_403_if_not_manager_or_maintenance(self):
        self.client.login(username="noprivilages", password="zaq1@WSX")
        response = self.client.get(
            (reverse("maintenance_reports_detail", kwargs={"pk": self.reports.pk}))
        )
        self.assertEqual(response.status_code, 403)
