from django.urls import reverse
from machines.tests.test_models import MachineTestUtils
from rest_framework import status
from rest_framework.test import APITestCase
from departments.models import Department
from machines.models.machine_group import MachineGroup
from machines.models.machine import Machine
from dashboard.tests import UserTestUtils


class TestAPIMachines(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.department = Department.objects.create(name="test")
        cls.machine_group = MachineGroup.objects.create(name="test")
        cls.user = UserTestUtils.create_user(group="manager", department=cls.department)
        cls.user_noprivilages = UserTestUtils.create_user(
            username="noprivilages", department=cls.department
        )
        machine_id = MachineTestUtils.create_machine(
            department=cls.department, machine_group=cls.machine_group
        ).pk

        cls.urls = [
            "/api/machines/",
            f"/api/machines/{machine_id}/",
        ]

        cls.named_urls = [
            reverse("machines"),
            reverse("machines-detail", kwargs={"pk": machine_id}),
        ]

    def test_create_machine(self):
        self.machine = {
            "factory_number": "111",
            "name": "test",
            "machine_group": f"{self.machine_group.pk}",
            "department": f"{self.department.pk}",
            "number": "99",
            "producer": "test",
        }
        self.client.force_authenticate(user=self.user)
        response = self.client.post(reverse("machines-list"), self.machine)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Machine.objects.count(), 2)

    def test_patch_machine(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.patch(
            reverse("machines-detail", kwargs={"pk": 1}), {"factory_number": "999"}
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Machine.objects.get(pk=1).factory_number, "999")

    def test_delete_machine(self):
        machine_id = MachineTestUtils.create_machine().pk
        self.client.force_authenticate(user=self.user)
        response = self.client.delete(
            reverse("machines-detail", kwargs={"pk": machine_id})
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Machine.objects.count(), 1)

    def test_API_urls_exists_at_desired_location(self):
        self.client.login(username="test1", password=UserTestUtils.user_password)
        for url in self.urls:
            self.assertEqual(self.client.get(url).status_code, status.HTTP_200_OK)

    def test_API_accessible_by_url_name(self):
        self.client.login(username="test1", password=UserTestUtils.user_password)
        for url in self.named_urls:
            self.assertEqual(self.client.get(url).status_code, status.HTTP_200_OK)
