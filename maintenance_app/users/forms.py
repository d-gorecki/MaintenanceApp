from django.contrib.auth.forms import UserCreationForm
from .models import User


class ManagerUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            "username",
            "password1",
            "password2",
            "group",
            "first_name",
            "last_name",
            "department",
            "email",
            "function",
            "mobile",
        )
