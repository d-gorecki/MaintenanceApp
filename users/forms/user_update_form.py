from django import forms

from users.models import User


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model: User = User
        fields: tuple[str] = (
            "username",
            "group",
            "first_name",
            "last_name",
            "department",
            "email",
            "function",
            "mobile",
        )
