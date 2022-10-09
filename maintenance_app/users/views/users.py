from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from ..models import User


class Users(LoginRequiredMixin, ListView):
    model = User
    context_object_name = "users"
    template_name = "users/users.html"
