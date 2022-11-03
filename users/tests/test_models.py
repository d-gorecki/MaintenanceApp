from django.test import TestCase
from dashboard.tests import UserTestUtils


class TestUser(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = UserTestUtils.create_user()

    def test_first_name_max_length(self):
        user = self.user
        field_label = user._meta.get_field("first_name").verbose_name
        self.assertEqual(field_label, "first name")

    def test_last_name_max_length(self):
        user = self.user
        field_label = user._meta.get_field("last_name").verbose_name
        self.assertEqual(field_label, "last name")

    def test_group_max_length(self):
        user = self.user
        max_length = user._meta.get_field("group").max_length
        self.assertEqual(max_length, 20)

    def test_department_label(self):
        user = self.user
        field_label = user._meta.get_field("department").verbose_name
        self.assertEqual(field_label, "department")

    def test_mobile_label(self):
        user = self.user
        field_label = user._meta.get_field("mobile").verbose_name
        self.assertEqual(field_label, "mobile")

    def test_mobile_max_length(self):
        user = self.user
        max_length = user._meta.get_field("mobile").max_length
        self.assertEqual(max_length, 12)

    def test_function_label(self):
        user = self.user
        field_label = user._meta.get_field("function").verbose_name
        self.assertEqual(field_label, "function")

    def test_function_max_length(self):
        user = self.user
        max_length = user._meta.get_field("function").max_length
        self.assertEqual(max_length, 50)
