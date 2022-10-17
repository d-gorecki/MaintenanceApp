from django.test import TestCase
from departments.models import Department
from users.models import User
from django.urls import reverse


class UsersBaseViewTest(TestCase):
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
        response = self.client.get("/users/")
        self.assertEqual(response.status_code, 200)

    def test_accessible_by_url_name(self):
        self.client.login(username="test1", password="zaq1@WSX")
        response = self.client.get((reverse("users")))
        self.assertEqual(response.status_code, 200)

    def test_uses_correct_template(self):
        self.client.login(username="test1", password="zaq1@WSX")
        response = self.client.get((reverse("users")))
        self.assertTemplateUsed(response, "users/users.html")

    def test_redirect_if_not_logged_in(self):
        response = self.client.get((reverse("users")))
        self.assertRedirects(response, "/users/login/?next=/users/")

    def test_displays_proper_list_of_objects(self):
        self.client.login(username="test1", password="zaq1@WSX")
        response = self.client.get((reverse("users")))
        self.assertEqual(len(response.context["users"]), 3)

    def test_403_if_not_manager(self):
        self.client.login(username="noprivilages", password="zaq1@WSX")
        response = self.client.get((reverse("users")))
        self.assertEqual(response.status_code, 403)


class UsersUpdateViewTest(TestCase):
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

        cls.user_id = User.objects.create_user(
            username="noprivilages",
            password="zaq1@WSX",
            department=department_2,
            group="production",
        ).pk

    def test_url_exists_at_desired_location(self):
        self.client.login(username="test1", password="zaq1@WSX")
        response = self.client.get(f"/users/edit/{self.user_id}/")
        self.assertEqual(response.status_code, 200)

    def test_accessible_by_url_name(self):
        self.client.login(username="test1", password="zaq1@WSX")
        response = self.client.get((reverse("users_edit", kwargs={"pk": self.user_id})))
        self.assertEqual(response.status_code, 200)

    def test_uses_correct_template(self):
        self.client.login(username="test1", password="zaq1@WSX")
        response = self.client.get((reverse("users_edit", kwargs={"pk": self.user_id})))
        self.assertTemplateUsed(response, "users/users_edit.html")

    def test_redirect_if_not_logged_in(self):
        response = self.client.get((reverse("users_edit", kwargs={"pk": self.user_id})))
        self.assertRedirects(
            response, f"/users/login/?next=/users/edit/{self.user_id}/"
        )

    def test_403_if_not_manager(self):
        self.client.login(username="noprivilages", password="zaq1@WSX")
        response = self.client.get((reverse("users_edit", kwargs={"pk": self.user_id})))
        self.assertEqual(response.status_code, 403)
