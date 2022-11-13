from django.test import TestCase
from django.urls import reverse
from rest_framework import status

from departments.models import Department
from users.models import User


class UserTestUtils:
    user_password = "zaq1@WSX"

    @staticmethod
    def create_user(
        username="test1",
        password=user_password,
        department=None,
        group="production",
        email="testemail@gmail.com",
        first_name="Test",
        last_name="Test",
        function="electrican",
        mobile="777777777",
    ):
        if not department:
            from departments.models import Department

            department = Department.objects.create(name="test")
        return User.objects.create_user(
            username=username,
            password=password,
            department=department,
            group=group,
            email=email,
            first_name=first_name,
            last_name=last_name,
            function=function,
            mobile=mobile,
        )


class TestDashboardView(TestCase):
    @classmethod
    def setUpTestData(cls):
        Department.objects.create(name="Test")
        UserTestUtils.create_user(group="manager")
        UserTestUtils.create_user(username="noprivilages", group="production")

    def test_dashboard_url_exists_at_desired_location(self):
        self.client.login(username="test1", password=UserTestUtils.user_password)
        response = self.client.get("/dashboard/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_dashboard_accessible_by_url_name(self):
        self.client.login(username="test1", password=UserTestUtils.user_password)
        response = self.client.get((reverse("dashboard")))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_dashboard_uses_correct_template(self):
        self.client.login(username="test1", password=UserTestUtils.user_password)
        response = self.client.get((reverse("dashboard")))
        self.assertTemplateUsed(response, "dashboard/dashboard.html")

    def test_dashboard_redirect_if_not_logged_in(self):
        response = self.client.get((reverse("dashboard")))
        self.assertRedirects(response, "/users/login/?next=/dashboard/")

    def test_dashboard_403_if_not_manager(self):
        self.client.login(username="noprivilages", password=UserTestUtils.user_password)
        response = self.client.get((reverse("dashboard")))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
