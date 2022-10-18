from django.test import TestCase
from django.urls import reverse

from departments.models import Department
from users.models import User
from machines.models.machine_group import MachineGroup
from machines.models.machine import Machine
from django.utils.timezone import now as django_now
from enum import Enum
from API.serializers import MachineGroupSerializer


class HttpResponseStatus(Enum):
    OK = 200
    FORBIDDEN = 403

    def __str__(self):
        return str(self.value)


class APIViewTest(TestCase):
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
        cls.machine_group = MachineGroup.objects.create(name="test")
        cls.machine_group_id = cls.machine_group.pk
        cls.machine = Machine.objects.create(
            factory_number="11111",
            machine_group=cls.machine_group,
            name="Test-name",
            number="1111",
            producer="test",
            purchase_data=django_now(),
            department=department,
            machine_status="available",
        )
        cls.machine_id = cls.machine.pk

        cls.urls = [
            "/api/machines/",
            f"/api/machines/{cls.machine_id}/",
            f"/api/machine_groups/{cls.machine_group_id}/",
            f"/api/machine/update/{cls.machine_id}/",
        ]

        cls.named_urls = [
            reverse("get_machines"),
            reverse("get_machine", kwargs={"pk": cls.machine_id}),
            reverse("get_machines_groups", kwargs={"pk": cls.machine_group_id}),
            reverse("update_machine", kwargs={"pk": cls.machine_id}),
        ]

    def test_API_urls_exists_at_desired_location(self):
        self.client.login(username="test1", password="zaq1@WSX")
        for url in self.urls:
            self.assertEqual(
                self.client.get(url).status_code, HttpResponseStatus.OK.value
            )

    def test_API_accessible_by_url_name(self):
        self.client.login(username="test1", password="zaq1@WSX")
        for url in self.named_urls:
            self.assertEqual(
                self.client.get(url).status_code, HttpResponseStatus.OK.value
            )

    def test_API_response_if_not_logged_in(self):
        for url in self.urls:
            self.assertEqual(
                self.client.get(url).status_code, HttpResponseStatus.FORBIDDEN.value
            )

    def test_API_response_if_no_privilages(self):
        self.client.login(username="noprivilages", password="zaq1@WSX")
        for url in self.urls[2:]:
            self.assertEqual(
                self.client.get(url).status_code, HttpResponseStatus.FORBIDDEN.value
            )
