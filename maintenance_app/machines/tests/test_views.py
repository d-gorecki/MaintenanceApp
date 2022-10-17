from django.test import TestCase
from django.urls import reverse
from departments.models import Department
from users.models import User
from machines.models.machine_group import MachineGroup
from machines.models.machine import Machine


class MachinesBaseViewTest(TestCase):
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

        machine_group = MachineGroup.objects.create(name="test")
        Machine.objects.create(
            factory_number="1", machine_group=machine_group, department=department_1
        )
        Machine.objects.create(
            factory_number="2", machine_group=machine_group, department=department_2
        )

    def test_url_exists_at_desired_location(self):
        self.client.login(username="test1", password="zaq1@WSX")
        response = self.client.get("")
        self.assertEqual(response.status_code, 200)

    def test_accessible_by_url_name(self):
        self.client.login(username="test1", password="zaq1@WSX")
        response = self.client.get((reverse("machines")))
        self.assertEqual(response.status_code, 200)

    def test_uses_correct_template(self):
        self.client.login(username="test1", password="zaq1@WSX")
        response = self.client.get((reverse("machines")))
        self.assertTemplateUsed(response, "machines/machines.html")

    def test_redirect_if_not_logged_in(self):
        response = self.client.get((reverse("machines")))
        self.assertRedirects(response, "/users/login/?next=/machines/")

    def test_displays_machines_for_particular_department(self):
        self.client.login(username="test2", password="zaq1@WSX")
        response = self.client.get((reverse("machines")))
        self.assertEqual(len(response.context["machines"]), 1)

    def test_displays_all_machines_for_manager(self):
        self.client.login(username="test1", password="zaq1@WSX")
        response = self.client.get((reverse("machines")))
        self.assertEqual(len(response.context["machines"]), 2)


class MachinesAddViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        department_1 = Department.objects.create(name="Department1")
        User.objects.create_user(
            username="test1",
            password="zaq1@WSX",
            department=department_1,
            group="manager",
        )

        User.objects.create_user(
            username="noprivilages",
            password="zaq1@WSX",
            department=department_1,
            group="production",
        )

    def test_url_exists_at_desired_location(self):
        self.client.login(username="test1", password="zaq1@WSX")
        response = self.client.get("/machines/add/")
        self.assertEqual(response.status_code, 200)

    def test_accessible_by_url_name(self):
        self.client.login(username="test1", password="zaq1@WSX")
        response = self.client.get((reverse("machines_add")))
        self.assertEqual(response.status_code, 200)

    def test_uses_correct_template(self):
        self.client.login(username="test1", password="zaq1@WSX")
        response = self.client.get((reverse("machines_add")))
        self.assertTemplateUsed(response, "machines/machines_add.html")

    def test_redirect_if_not_logged_in(self):
        response = self.client.get((reverse("machines_add")))
        self.assertRedirects(response, "/users/login/?next=/machines/add/")

    def test_403_if_not_manager(self):
        self.client.login(username="noprivilages", password="zaq1@WSX")
        response = self.client.get((reverse("machines_add")))
        self.assertEqual(response.status_code, 403)


class MachinesEditViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        department_1 = Department.objects.create(name="Department1")
        User.objects.create_user(
            username="test1",
            password="zaq1@WSX",
            department=department_1,
            group="manager",
        )

        User.objects.create_user(
            username="noprivilages",
            password="zaq1@WSX",
            department=department_1,
            group="production",
        )

        machine_group = MachineGroup.objects.create(name="test")
        cls.machine_id = Machine.objects.create(
            factory_number="1", machine_group=machine_group, department=department_1
        ).pk

    def test_url_exists_at_desired_location(self):
        self.client.login(username="test1", password="zaq1@WSX")
        response = self.client.get(f"/machines/edit/{self.machine_id}/")
        self.assertEqual(response.status_code, 200)

    def test_accessible_by_url_name(self):
        self.client.login(username="test1", password="zaq1@WSX")
        response = self.client.get(
            (reverse("machines_edit", kwargs={"pk": self.machine_id}))
        )
        self.assertEqual(response.status_code, 200)

    def test_uses_correct_template(self):
        self.client.login(username="test1", password="zaq1@WSX")
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
        self.client.login(username="noprivilages", password="zaq1@WSX")
        response = self.client.get(
            (reverse("machines_edit", kwargs={"pk": self.machine_id}))
        )
        self.assertEqual(response.status_code, 403)
