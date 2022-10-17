from django.test import TestCase
from machines.models.machine import Machine
from machines.models.machine_group import MachineGroup
from datetime import datetime
from departments.models import Department
from django.utils.timezone import now as django_now


class MachineGroupTest(TestCase):
    @classmethod
    def setUp(cls):
        cls.obj_id = MachineGroup.objects.create(name="Test-group").pk

    def test_name_label(self):
        name = MachineGroup.objects.get(id=self.obj_id)
        field_label = name._meta.get_field("name").verbose_name
        self.assertEqual(field_label, "name")

    def test_name_max_length(self):
        name = MachineGroup.objects.get(id=self.obj_id)
        max_length = name._meta.get_field("name").max_length
        self.assertEqual(max_length, 100)

    def test_obj_str_is_name(self):
        name = MachineGroup.objects.get(id=self.obj_id)
        expected_obj_str = f"{name.name}"
        self.assertEqual(str(name), expected_obj_str)


class MachineTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.group_id = MachineGroup.objects.create(name="Test-group").pk
        cls.department_id = Department.objects.create(name="Test-department").pk
        cls.obj_id = Machine.objects.create(
            factory_number="11111",
            machine_group=MachineGroup.objects.get(id=cls.group_id),
            name="Test-name",
            number="1111",
            producer="test",
            purchase_data=django_now(),
            department=Department.objects.get(id=cls.department_id),
            machine_status="available",
        ).pk

    def test_factory_number_label(self):
        factory_number = Machine.objects.get(id=self.obj_id)
        field_label = factory_number._meta.get_field("factory_number").verbose_name
        self.assertEqual(field_label, "factory number")

    def test_name_max_length(self):
        factory_number = Machine.objects.get(id=self.obj_id)
        max_length = factory_number._meta.get_field("factory_number").max_length
        self.assertEqual(max_length, 100)

    def test_machine_group_label(self):
        machine_group = Machine.objects.get(id=self.obj_id)
        field_label = machine_group._meta.get_field("machine_group").verbose_name
        self.assertEqual(field_label, "machine group")

    def test_name_label(self):
        name = Machine.objects.get(id=self.obj_id)
        field_label = name._meta.get_field("name").verbose_name
        self.assertEqual(field_label, "name")

    def test_name_max_length(self):
        name = Machine.objects.get(id=self.obj_id)
        max_length = name._meta.get_field("name").max_length
        self.assertEqual(max_length, 100)

    def test_number_label(self):
        number = Machine.objects.get(id=self.obj_id)
        field_label = number._meta.get_field("number").verbose_name
        self.assertEqual(field_label, "number")

    def test_number_max_length(self):
        number = Machine.objects.get(id=self.obj_id)
        max_length = number._meta.get_field("number").max_length
        self.assertEqual(max_length, 100)

    def test_producer_label(self):
        machine = Machine.objects.get(id=self.obj_id)
        field_label = machine._meta.get_field("producer").verbose_name
        self.assertEqual(field_label, "producer")

    def test_producer_max_length(self):
        machine = Machine.objects.get(id=self.obj_id)
        max_length = machine._meta.get_field("producer").max_length
        self.assertEqual(max_length, 100)

    def test_purchase_data_label(self):
        machine = Machine.objects.get(id=self.obj_id)
        field_label = machine._meta.get_field("purchase_data").verbose_name
        self.assertEqual(field_label, "purchase data")

    def test_department_label(self):
        machine = Machine.objects.get(id=self.obj_id)
        field_label = machine._meta.get_field("department").verbose_name
        self.assertEqual(field_label, "department")

    def test_machine_status_label(self):
        machine = Machine.objects.get(id=self.obj_id)
        field_label = machine._meta.get_field("machine_status").verbose_name
        self.assertEqual(field_label, "machine status")

    def test_machine_status_max_length(self):
        machine = Machine.objects.get(id=self.obj_id)
        max_length = machine._meta.get_field("machine_status").max_length
        self.assertEqual(max_length, 32)

    def test_obj_str_is_name(self):
        machine = Machine.objects.get(id=self.obj_id)
        expected_obj_str = f"{machine.factory_number}: {machine.name}"
        self.assertEqual(str(machine), expected_obj_str)
