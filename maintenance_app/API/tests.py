from django.test import TestCase
from django.urls import reverse
from machines.models.machine_group import MachineGroup
from dashboard.tests import UserTestUtils
from machines.tests.test_models import MachineTestUtils
from rest_framework import status


class APIViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        UserTestUtils.create_user(group="manager")
        UserTestUtils.create_user(username="noprivilages")
        machine_group = MachineGroup.objects.create(name="test")
        machine_id = MachineTestUtils.create_machine(machine_group=machine_group).pk

        cls.urls = [
            "/api/machines/",
            f"/api/machines/{machine_id}/",
            f"/api/machine_groups/{machine_group.pk}/",
            f"/api/machine/update/{machine_id}/",
        ]

        cls.named_urls = [
            reverse("get_machines"),
            reverse("get_machine", kwargs={"pk": machine_id}),
            reverse("get_machines_groups", kwargs={"pk": machine_group.pk}),
            reverse("update_machine", kwargs={"pk": machine_id}),
        ]

    def test_API_urls_exists_at_desired_location(self):
        self.client.login(username="test1", password=UserTestUtils.user_password)
        for url in self.urls:
            self.assertEqual(self.client.get(url).status_code, status.HTTP_200_OK)

    def test_API_accessible_by_url_name(self):
        self.client.login(username="test1", password=UserTestUtils.user_password)
        for url in self.named_urls:
            self.assertEqual(self.client.get(url).status_code, status.HTTP_200_OK)

    def test_API_response_if_not_logged_in(self):
        for url in self.urls:
            self.assertEqual(
                self.client.get(url).status_code, status.HTTP_403_FORBIDDEN
            )

    def test_API_response_if_no_privilages(self):
        self.client.login(username="noprivilages", password=UserTestUtils.user_password)
        for url in self.urls[2:]:
            self.assertEqual(
                self.client.get(url).status_code, status.HTTP_403_FORBIDDEN
            )
