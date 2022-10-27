from django.test import TestCase
from departments.models import Department


class TestDepartment(TestCase):
    def setUp(self):
        self.department = Department.objects.create(name="test-department")

    def test_name_label(self):
        department = self.department
        field_label = department._meta.get_field("name").verbose_name
        self.assertEqual(field_label, "name")

    def test_name_max_length(self):
        department = self.department
        max_length = department._meta.get_field("name").max_length
        self.assertEqual(max_length, 32)

    def test_obj_str_method_returns_name(self):
        dep = self.department
        expected_obj_str = f"{dep.name}"
        self.assertEqual(str(dep), expected_obj_str)
