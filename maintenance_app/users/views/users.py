from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from ..models import User
from maintenance_app.mixins import ManagerGroupTestMixin


class Users(LoginRequiredMixin, ManagerGroupTestMixin, ListView):
    model = User
    context_object_name = "users"
    template_name = "users/users.html"
