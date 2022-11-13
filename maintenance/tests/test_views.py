from django.test import TestCase
from django.urls import reverse
from django.utils.timezone import now as django_now
from django.utils.timezone import timedelta
from rest_framework import status

from dashboard.tests import UserTestUtils
from maintenance.tests.test_models import MaintenanceTestUtils


class TestMaintenanceReportsBaseView(TestCase):
    @classmethod
    def setUpTestData(cls):
        UserTestUtils.create_user(group="manager")
        UserTestUtils.create_user(username="noprivilages")
        users = [UserTestUtils.create_user(username=f"test_{i}") for i in range(5)]
        schedules = [
            MaintenanceTestUtils.create_maintenance_schedule(
                planned_date=django_now() + timedelta(i), user=users[i]
            )
            for i in range(5)
        ]
        [
            MaintenanceTestUtils.create_maintenance_report(
                schedule=schedules[i], user=users[i]
            )
            for i in range(3)
        ]

    def test_url_exists_at_desired_location(self):
        self.client.login(username="test1", password=UserTestUtils.user_password)
        response = self.client.get("/maintenance/schedules/reports/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_accessible_by_url_name(self):
        self.client.login(username="test1", password=UserTestUtils.user_password)
        response = self.client.get((reverse("maintenance_reports")))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_uses_correct_template(self):
        self.client.login(username="test1", password=UserTestUtils.user_password)
        response = self.client.get((reverse("maintenance_reports")))
        self.assertTemplateUsed(response, "maintenance/maintenance_reports.html")

    def test_redirect_if_not_logged_in(self):
        response = self.client.get((reverse("maintenance_reports")))
        self.assertRedirects(
            response, "/users/login/?next=/maintenance/schedules/reports/"
        )

    def test_displays_proper_list_of_objects(self):
        self.client.login(username="test1", password=UserTestUtils.user_password)
        response = self.client.get((reverse("maintenance_reports")))
        self.assertEqual(len(response.context["reports"]), 3)

    def test_403_if_not_manager(self):
        self.client.login(username="noprivilages", password=UserTestUtils.user_password)
        response = self.client.get((reverse("maintenance_reports")))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class MaintenanceReportsCreateViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        UserTestUtils.create_user(group="manager")
        UserTestUtils.create_user(username="noprivilages")

    def test_url_exists_at_desired_location(self):
        self.client.login(username="test1", password=UserTestUtils.user_password)
        response = self.client.get("/maintenance/schedules/reports/add")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_accessible_by_url_name(self):
        self.client.login(username="test1", password=UserTestUtils.user_password)
        response = self.client.get((reverse("maintenance_reports_add")))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_uses_correct_template(self):
        self.client.login(username="test1", password=UserTestUtils.user_password)
        response = self.client.get((reverse("maintenance_reports_add")))
        self.assertTemplateUsed(response, "maintenance/maintenance_reports_add.html")

    def test_redirect_if_not_logged_in(self):
        response = self.client.get((reverse("maintenance_reports_add")))
        self.assertRedirects(
            response, "/users/login/?next=/maintenance/schedules/reports/add"
        )

    def test_403_if_not_manager(self):
        self.client.login(username="noprivilages", password=UserTestUtils.user_password)
        response = self.client.get((reverse("maintenance_reports_add")))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class MaintenanceReportsDetailViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        user_1 = UserTestUtils.create_user(group="maintenance")
        UserTestUtils.create_user(username="noprivilages")
        cls.reports = MaintenanceTestUtils.create_maintenance_report(user=user_1)

    def test_url_exists_at_desired_location(self):
        self.client.login(username="test1", password=UserTestUtils.user_password)
        response = self.client.get(f"/maintenance/schedules/reports/{self.reports.pk}")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_accessible_by_url_name(self):
        self.client.login(username="test1", password=UserTestUtils.user_password)
        response = self.client.get(
            (reverse("maintenance_reports_detail", kwargs={"pk": self.reports.pk}))
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_uses_correct_template(self):
        self.client.login(username="test1", password=UserTestUtils.user_password)
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
        self.client.login(username="noprivilages", password=UserTestUtils.user_password)
        response = self.client.get(
            (reverse("maintenance_reports_detail", kwargs={"pk": self.reports.pk}))
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
