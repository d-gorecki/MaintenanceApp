from users.models import User
from django import forms


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
