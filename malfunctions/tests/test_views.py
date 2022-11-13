from django.test import TestCase
from django.urls import reverse
from rest_framework import status

from dashboard.tests import UserTestUtils
from malfunctions.tests.test_models import MalfunctionTestUtils


class TestMalfunctionPendingView(TestCase):
    @classmethod
    def setUpTestData(cls):
        UserTestUtils.create_user(username="noprivilages")
        user = UserTestUtils.create_user(group="manager")
        cls.malfunction_reports = [
            MalfunctionTestUtils.create_malfunction_report(user=user) for _ in range(3)
        ]

    def test_url_exists_at_desired_location(self):
        self.client.login(username="test1", password=UserTestUtils.user_password)
        response = self.client.get("/malfunctions/pending/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_accessible_by_url_name(self):
        self.client.login(username="test1", password=UserTestUtils.user_password)
        response = self.client.get((reverse("malfunctions_pending")))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_uses_correct_template(self):
        self.client.login(username="test1", password=UserTestUtils.user_password)
        response = self.client.get((reverse("malfunctions_pending")))
        self.assertTemplateUsed(response, "malfunctions/malfunctions_pending.html")

    def test_redirect_if_not_logged_in(self):
        response = self.client.get((reverse("malfunctions_pending")))
        self.assertRedirects(response, "/users/login/?next=/malfunctions/pending/")

    def test_displays_proper_list_of_objects(self):
        self.client.login(username="test1", password=UserTestUtils.user_password)
        response = self.client.get((reverse("malfunctions_pending")))
        self.assertEqual(len(response.context["malfunctions"]), 3)

    def test_403_if_not_manager(self):
        self.client.login(username="noprivilages", password=UserTestUtils.user_password)
        response = self.client.get((reverse("malfunctions_pending")))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class TestMalfunctionServicesBase(TestCase):
    @classmethod
    def setUpTestData(cls):

        UserTestUtils.create_user(username="noprivilages")
        user = UserTestUtils.create_user(group="manager")
        malfunction_reports = [
            MalfunctionTestUtils.create_malfunction_report(user=user) for _ in range(3)
        ]
        [
            MalfunctionTestUtils.create_service_report(
                malfunction_report=malfunction_reports[i], user=user, service="finished"
            )
            for i in range(3)
        ]

    def test_url_exists_at_desired_location(self):
        self.client.login(username="test1", password=UserTestUtils.user_password)
        response = self.client.get("/malfunctions/services/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_accessible_by_url_name(self):
        self.client.login(username="test1", password=UserTestUtils.user_password)
        response = self.client.get((reverse("malfunctions_services")))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_uses_correct_template(self):
        self.client.login(username="test1", password=UserTestUtils.user_password)
        response = self.client.get((reverse("malfunctions_services")))
        self.assertTemplateUsed(response, "malfunctions/malfunctions_services.html")

    def test_redirect_if_not_logged_in(self):
        response = self.client.get((reverse("malfunctions_services")))
        self.assertRedirects(response, "/users/login/?next=/malfunctions/services/")

    def test_displays_proper_list_of_objects(self):
        self.client.login(username="test1", password=UserTestUtils.user_password)
        response = self.client.get((reverse("malfunctions_services")))
        self.assertEqual(len(response.context["services"]), 3)

    def test_403_if_not_manager(self):
        self.client.login(username="noprivilages", password=UserTestUtils.user_password)
        response = self.client.get((reverse("malfunctions_pending")))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
