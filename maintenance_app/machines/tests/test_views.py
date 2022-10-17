from django.test import TestCase
from django.urls import reverse
from departments.models import Department
from users.models import User
from machines.models.machine_group import MachineGroup
from machines.models.machine import Machine
from django.utils.timezone import now as django_now


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
        cls.department_1 = Department.objects.create(name="Department1")
        User.objects.create_user(
            username="test1",
            password="zaq1@WSX",
            department=cls.department_1,
            group="manager",
        )

        User.objects.create_user(
            username="noprivilages",
            password="zaq1@WSX",
            department=cls.department_1,
            group="production",
        )

        cls.machine_group = MachineGroup.objects.create(name="test")

        cls.form_data = {
            "factory_number": "1",
            "machine_group": cls.machine_group,
            "name": "111",
            "number": "111",
            "producer": "test",
            "department": cls.department_1,
            "machine_status": "available",
        }

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
        cls.department_id = Department.objects.create(name="Department1").pk
        User.objects.create_user(
            username="test1",
            password="zaq1@WSX",
            department=Department.objects.get(pk=cls.department_id),
            group="manager",
        )

        User.objects.create_user(
            username="noprivilages",
            password="zaq1@WSX",
            department=Department.objects.get(pk=cls.department_id),
            group="production",
        )

        cls.group_id = MachineGroup.objects.create(name="test").pk
        cls.machine_id = Machine.objects.create(
            factory_number="11111",
            machine_group=MachineGroup.objects.get(id=cls.group_id),
            name="Test-name",
            number="1111",
            producer="test",
            purchase_data=django_now(),
            department=Department.objects.get(id=cls.department_id),
            machine_status="available",
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
