from django.test import TestCase
from django.urls import reverse
from users.models import User
from departments.models import Department


class DashboardViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        department = Department.objects.create(name="Test")
        User.objects.create_user(
            username="test1",
            password="zaq1@WSX",
            department=department,
            group="manager",
        )
        User.objects.create_user(
            username="noprivilages",
            password="zaq1@WSX",
            department=department,
            group="production",
        )

    def test_dashboard_url_exists_at_desired_location(self):
        self.client.login(username="test1", password="zaq1@WSX")
        response = self.client.get("/dashboard/")
        self.assertEqual(response.status_code, 200)

    def test_dashboard_accessible_by_url_name(self):
        self.client.login(username="test1", password="zaq1@WSX")
        response = self.client.get((reverse("dashboard")))
        self.assertEqual(response.status_code, 200)

    def test_dashboard_uses_correct_template(self):
        self.client.login(username="test1", password="zaq1@WSX")
        response = self.client.get((reverse("dashboard")))
        self.assertTemplateUsed(response, "dashboard/dashboard.html")

    def test_dashboard_redirect_if_not_logged_in(self):
        response = self.client.get((reverse("dashboard")))
        self.assertRedirects(response, "/users/login/?next=/dashboard/")

    def test_dashboard_403_if_not_manager(self):
        self.client.login(username="noprivilages", password="zaq1@WSX")
        response = self.client.get((reverse("dashboard")))
        self.assertEqual(response.status_code, 403)
