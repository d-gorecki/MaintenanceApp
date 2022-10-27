from django.test import TestCase
from django.urls import reverse
from departments.models import Department
from machines.models.machine_group import MachineGroup
from dashboard.tests import UserTestUtils
from machines.tests.test_models import MachineTestUtils
from rest_framework import status


class TestMachinesBaseView(TestCase):
    @classmethod
    def setUpTestData(cls):
        department_1 = Department.objects.create(name="Department1")
        department_2 = Department.objects.create(name="Department2")
        UserTestUtils.create_user(
            username="test1", department=department_1, group="manager"
        )
        UserTestUtils.create_user(username="test2", department=department_2)
        MachineTestUtils.create_machine(department=department_1)
        MachineTestUtils.create_machine(department=department_2)

    def test_url_exists_at_desired_location(self):
        self.client.login(username="test1", password=UserTestUtils.user_password)
        response = self.client.get("/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_accessible_by_url_name(self):
        self.client.login(username="test1", password=UserTestUtils.user_password)
        response = self.client.get((reverse("machines")))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_uses_correct_template(self):
        self.client.login(username="test1", password=UserTestUtils.user_password)
        response = self.client.get((reverse("machines")))
        self.assertTemplateUsed(response, "machines/machines.html")

    def test_redirect_if_not_logged_in(self):
        response = self.client.get((reverse("machines")))
        self.assertRedirects(response, "/users/login/?next=/machines/")

    def test_displays_machines_for_particular_department(self):
        self.client.login(username="test2", password=UserTestUtils.user_password)
        response = self.client.get((reverse("machines")))
        self.assertEqual(len(response.context["machines"]), 1)

    def test_displays_all_machines_for_manager(self):
        self.client.login(username="test1", password=UserTestUtils.user_password)
        response = self.client.get((reverse("machines")))
        self.assertEqual(len(response.context["machines"]), 2)


class TestMachinesAddView(TestCase):
    @classmethod
    def setUpTestData(cls):
        UserTestUtils.create_user(group="manager")
        UserTestUtils.create_user(username="noprivilages")
        cls.form_data = {
            "factory_number": "1",
            "machine_group": MachineGroup.objects.create(name="test"),
            "name": "111",
            "number": "111",
            "producer": "test",
            "department": Department.objects.create(name="Department1"),
            "machine_status": "available",
        }

    def test_url_exists_at_desired_location(self):
        self.client.login(username="test1", password=UserTestUtils.user_password)
        response = self.client.get("/machines/add/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_accessible_by_url_name(self):
        self.client.login(username="test1", password=UserTestUtils.user_password)
        response = self.client.get((reverse("machines_add")))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_uses_correct_template(self):
        self.client.login(username="test1", password=UserTestUtils.user_password)
        response = self.client.get((reverse("machines_add")))
        self.assertTemplateUsed(response, "machines/machines_add.html")

    def test_redirect_if_not_logged_in(self):
        response = self.client.get((reverse("machines_add")))
        self.assertRedirects(response, "/users/login/?next=/machines/add/")

    def test_403_if_not_manager(self):
        self.client.login(username="noprivilages", password=UserTestUtils.user_password)
        response = self.client.get((reverse("machines_add")))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class TestMachinesEditView(TestCase):
    @classmethod
    def setUpTestData(cls):
        UserTestUtils.create_user(group="manager")
        UserTestUtils.create_user(username="noprivilages")
        cls.machine_id = MachineTestUtils.create_machine().pk

    def test_url_exists_at_desired_location(self):
        self.client.login(username="test1", password=UserTestUtils.user_password)
        response = self.client.get(f"/machines/edit/{self.machine_id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_accessible_by_url_name(self):
        self.client.login(username="test1", password=UserTestUtils.user_password)
        response = self.client.get(
            (reverse("machines_edit", kwargs={"pk": self.machine_id}))
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_uses_correct_template(self):
        self.client.login(username="test1", password=UserTestUtils.user_password)
        response = self.client.get(
            (reverse("machines_edit", kwargs={"pk": self.machine_id}))
        )
        self.assertTemplateUsed(response, "machines/machines_edit.html")

    def test_redirect_if_not_logged_in(self):
        response = self.client.get(
            (reverse("machines_edit", kwargs={"pk": self.machine_id}))
        )
        self.assertRedirects(
            response, f"/users/login/?next=/machines/edit/{self.machine_id}/"
        )

    def test_403_if_not_manager(self):
        self.client.login(username="noprivilages", password=UserTestUtils.user_password)
        response = self.client.get(
            (reverse("machines_edit", kwargs={"pk": self.machine_id}))
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
