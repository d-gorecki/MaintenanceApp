from django.test import TestCase
from departments.models import Department


class DepartmentTest(TestCase):
    @classmethod
    def setUp(cls):
        cls.obj_id = Department.objects.create(name="test-department").pk

    def test_name_label(self):
        department = Department.objects.get(id=self.obj_id)
        field_label = department._meta.get_field("name").verbose_name
        self.assertEqual(field_label, "name")

    def test_name_max_length(self):
        department = Department.objects.get(id=self.obj_id)
        max_length = department._meta.get_field("name").max_length
        self.assertEqual(max_length, 32)

    def test_obj_str_metod_returns_name(self):
        dep = Department.objects.get(id=self.obj_id)
        expected_obj_str = f"{dep.name}"
        self.assertEqual(str(dep), expected_obj_str)
