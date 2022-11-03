from django.test import TestCase
from django.urls import reverse
from dashboard.tests import UserTestUtils
from rest_framework import status
from machines.tests.factory import (
    UserFactory,
    DepartmentFactory,
    MachineGroupFactory,
    MachineFactory,
)


class TestMachinesBaseView(TestCase):
    @classmethod
    def setUpTestData(cls):
        UserFactory.reset_sequence()
        MachineFactory.reset_sequence()
        DepartmentFactory.reset_sequence()
        cls.passwd = "zaq1@WSX"
        department_1 = DepartmentFactory()
        department_2 = DepartmentFactory()
        UserFactory()
        UserFactory(department=department_1, group="manager")
        UserFactory(department=department_2, group="production")
        MachineFactory.create(department=department_1)
        MachineFactory.create(department=department_2)

    def test_url_exists_at_desired_location(self):
        self.client.login(username="test1", password=self.passwd)
        response = self.client.get("/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_accessible_by_url_name(self):
        self.client.login(username="test1", password=self.passwd)
        response = self.client.get((reverse("machines")))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_uses_correct_template(self):
        self.client.login(username="test1", password=self.passwd)
        response = self.client.get((reverse("machines")))
        self.assertTemplateUsed(response, "machines/machines.html")

    def test_redirect_if_not_logged_in(self):
        response = self.client.get((reverse("machines")))
        self.assertRedirects(response, "/users/login/?next=/machines/")

    def test_displays_machines_for_particular_department(self):
        self.client.login(username="test2", password=self.passwd)
        response = self.client.get((reverse("machines")))
        self.assertEqual(len(response.context["machines"]), 1)

    def test_displays_all_machines_for_manager(self):
        self.client.login(username="test1", password=self.passwd)
        response = self.client.get((reverse("machines")))
        self.assertEqual(len(response.context["machines"]), 2)


class TestMachinesAddView(TestCase):
    @classmethod
    def setUpTestData(cls):
        UserFactory.reset_sequence()
        MachineGroupFactory.reset_sequence()
        DepartmentFactory.reset_sequence()
        UserFactory()
        UserFactory(group="manager")
        UserFactory(username="noprivilages")
        cls.form_data = {
            "factory_number": "1",
            "machine_group": MachineGroupFactory(),
            "name": "111",
            "number": "111",
            "producer": "test",
            "department": DepartmentFactory(),
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
        UserFactory.reset_sequence()
        MachineFactory.reset_sequence()
        UserFactory()
        UserFactory(group="manager")
        UserFactory(username="noprivilages")
        cls.machine_id = MachineFactory().pk

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
