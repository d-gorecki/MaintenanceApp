from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from ..models import User
from maintenance_app.mixins import ManagerGroupTestMixin


class Users(LoginRequiredMixin, ManagerGroupTestMixin, ListView):
    """Main(list) view for users app"""

    model: User = User
    context_object_name: str = "users"
    template_name: str = "users/users.html"
