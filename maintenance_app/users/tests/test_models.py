from users.models import User
from django.test import TestCase
from departments.models import Department


class UserTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        department = Department.objects.create(name="test")
        user = User.objects.create(
            username="test-user",
            first_name="test",
            last_name="test",
            department=department,
            group="manager",
            email="asd@google.com",
            function="electrican",
            mobile="777777777",
        )
        cls.user_id = user.pk

    def test_first_name_max_length(self):
        user = User.objects.get(pk=self.user_id)
        field_label = user._meta.get_field("first_name").verbose_name
        self.assertEqual(field_label, "first name")

    def test_last_name_max_length(self):
        user = User.objects.get(pk=self.user_id)
        field_label = user._meta.get_field("last_name").verbose_name
        self.assertEqual(field_label, "last name")

    def test_group_max_length(self):
        user = User.objects.get(pk=self.user_id)
        max_length = user._meta.get_field("group").max_length
        self.assertEqual(max_length, 20)

    def test_department_label(self):
        user = User.objects.get(pk=self.user_id)
        field_label = user._meta.get_field("department").verbose_name
        self.assertEqual(field_label, "department")

    def test_mobile_label(self):
        user = User.objects.get(pk=self.user_id)
        field_label = user._meta.get_field("mobile").verbose_name
        self.assertEqual(field_label, "mobile")

    def test_mobile_max_length(self):
        user = User.objects.get(pk=self.user_id)
        max_length = user._meta.get_field("mobile").max_length
        self.assertEqual(max_length, 12)

    def test_function_label(self):
        user = User.objects.get(pk=self.user_id)
        field_label = user._meta.get_field("function").verbose_name
        self.assertEqual(field_label, "function")


def test_function_max_length(self):
    user = User.objects.get(pk=self.user_id)
    max_length = user._meta.get_field("function").max_length
    self.assertEqual(max_length, 50)
