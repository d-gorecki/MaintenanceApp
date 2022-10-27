from django.test import TestCase
from django.urls import reverse
from dashboard.tests import UserTestUtils
from rest_framework import status


class TestUsersBaseView(TestCase):
    @classmethod
    def setUpTestData(cls):
        UserTestUtils.create_user(group="manager")
        UserTestUtils.create_user(username="noprivilages")
        UserTestUtils.create_user(username="user3")

    def test_url_exists_at_desired_location(self):
        self.client.login(username="test1", password=UserTestUtils.user_password)
        response = self.client.get("/users/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_accessible_by_url_name(self):
        self.client.login(username="test1", password=UserTestUtils.user_password)
        response = self.client.get((reverse("users")))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_uses_correct_template(self):
        self.client.login(username="test1", password=UserTestUtils.user_password)
        response = self.client.get((reverse("users")))
        self.assertTemplateUsed(response, "users/users.html")

    def test_redirect_if_not_logged_in(self):
        response = self.client.get((reverse("users")))
        self.assertRedirects(response, "/users/login/?next=/users/")

    def test_displays_proper_list_of_objects(self):
        self.client.login(username="test1", password=UserTestUtils.user_password)
        response = self.client.get((reverse("users")))
        self.assertEqual(len(response.context["users"]), 3)

    def test_403_if_not_manager(self):
        self.client.login(username="noprivilages", password=UserTestUtils.user_password)
        response = self.client.get((reverse("users")))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class TestUsersUpdateView(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user_id = UserTestUtils.create_user(group="manager").pk
        UserTestUtils.create_user(username="noprivilages")

    def test_url_exists_at_desired_location(self):
        self.client.login(username="test1", password=UserTestUtils.user_password)
        response = self.client.get(f"/users/edit/{self.user_id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_accessible_by_url_name(self):
        self.client.login(username="test1", password=UserTestUtils.user_password)
        response = self.client.get((reverse("users_edit", kwargs={"pk": self.user_id})))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_uses_correct_template(self):
        self.client.login(username="test1", password=UserTestUtils.user_password)
        response = self.client.get((reverse("users_edit", kwargs={"pk": self.user_id})))
        self.assertTemplateUsed(response, "users/users_edit.html")

    def test_redirect_if_not_logged_in(self):
        response = self.client.get((reverse("users_edit", kwargs={"pk": self.user_id})))
        self.assertRedirects(
            response, f"/users/login/?next=/users/edit/{self.user_id}/"
        )

    def test_403_if_not_manager(self):
        self.client.login(username="noprivilages", password=UserTestUtils.user_password)
        response = self.client.get((reverse("users_edit", kwargs={"pk": self.user_id})))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
