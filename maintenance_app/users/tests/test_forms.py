from django.test import TestCase
from users.forms.user_update_form import UserUpdateForm
from users.forms.manager_user_creation_form import ManagerUserCreationForm


class TestUserForms(TestCase):
    def test_user_update_form(self):
        form = UserUpdateForm()
        fields = [
            "group",
            "first_name",
            "last_name",
            "department",
            "email",
            "function",
            "mobile",
        ]
        for field in fields:
            self.assertIn(field, form.fields)

    def test_user_creation_form(self):
        form = ManagerUserCreationForm()
        fields = ["department", "email", "function", "mobile"]
        for field in fields:
            self.assertIn(field, form.fields)
