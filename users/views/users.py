from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from maintenance_app.mixins import ManagerGroupTestMixin

from ..models import User


class Users(LoginRequiredMixin, ManagerGroupTestMixin, ListView):
    """Main(list) view for users app"""

    model: User = User
    context_object_name: str = "users"
    template_name: str = "users/users.html"
