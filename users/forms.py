from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import User


class ManagerUserCreationForm(UserCreationForm):
    class Meta:
        model: User = User
        fields: tuple[str] = (
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
