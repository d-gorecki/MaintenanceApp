from django.test import TestCase

from machines.models.machine import Machine
from machines.models.machine_group import MachineGroup


class MachineTestUtils:
    @staticmethod
    def create_machine(
        factory_number="test",
        machine_group=None,
        name="test",
        number="test",
        producer="test",
        department=None,
        machine_status="available",
    ):
        from django.utils.timezone import now

        if not machine_group:
            from machines.models.machine_group import MachineGroup

            machine_group = MachineGroup.objects.create(name="test")
        if not department:
            from departments.models import Department

            department = Department.objects.create(name="test")

        return Machine.objects.create(
            factory_number=factory_number,
            machine_group=machine_group,
            name=name,
            number=number,
            producer=producer,
            department=department,
            machine_status=machine_status,
            purchase_data=now(),
        )


class TestMachineGroup(TestCase):
    @classmethod
    def setUp(cls):
        cls.machine_group = MachineGroup.objects.create(name="Test-group")

    def test_name_label(self):
        name = self.machine_group
        field_label = name._meta.get_field("name").verbose_name
        self.assertEqual(field_label, "name")

    def test_name_max_length(self):
        name = self.machine_group
        max_length = name._meta.get_field("name").max_length
        self.assertEqual(max_length, 100)

    def test_obj_str_is_name(self):
        name = self.machine_group
        expected_obj_str = f"{name.name}"
        self.assertEqual(str(name), expected_obj_str)


class TestMachine(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.machine = MachineTestUtils.create_machine()

    def test_factory_number_label(self):
        factory_number = self.machine
        field_label = factory_number._meta.get_field("factory_number").verbose_name
        self.assertEqual(field_label, "factory number")

    def test_name_max_length(self):
        factory_number = self.machine
        max_length = factory_number._meta.get_field("factory_number").max_length
        self.assertEqual(max_length, 100)

    def test_machine_group_label(self):
        machine_group = self.machine
        field_label = machine_group._meta.get_field("machine_group").verbose_name
        self.assertEqual(field_label, "machine group")

    def test_name_label(self):
        name = self.machine
        field_label = name._meta.get_field("name").verbose_name
        self.assertEqual(field_label, "name")

    def test_number_label(self):
        number = self.machine
        field_label = number._meta.get_field("number").verbose_name
        self.assertEqual(field_label, "number")

    def test_number_max_length(self):
        number = self.machine
        max_length = number._meta.get_field("number").max_length
        self.assertEqual(max_length, 100)

    def test_producer_label(self):
        machine = self.machine
        field_label = machine._meta.get_field("producer").verbose_name
        self.assertEqual(field_label, "producer")

    def test_producer_max_length(self):
        machine = self.machine
        max_length = machine._meta.get_field("producer").max_length
        self.assertEqual(max_length, 100)

    def test_purchase_data_label(self):
        machine = self.machine
        field_label = machine._meta.get_field("purchase_data").verbose_name
        self.assertEqual(field_label, "purchase data")

    def test_department_label(self):
        machine = self.machine
        field_label = machine._meta.get_field("department").verbose_name
        self.assertEqual(field_label, "department")

    def test_machine_status_label(self):
        machine = self.machine
        field_label = machine._meta.get_field("machine_status").verbose_name
        self.assertEqual(field_label, "machine status")

    def test_machine_status_max_length(self):
        machine = self.machine
        max_length = machine._meta.get_field("machine_status").max_length
        self.assertEqual(max_length, 32)

    def test_obj_str_is_name(self):
        machine = self.machine
        expected_obj_str = f"{machine.factory_number}: {machine.name}"
        self.assertEqual(str(machine), expected_obj_str)
