from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from users.forms.user_update_form import UserUpdateForm
from ..models import User
from maintenance_app.mixins import ManagerMaintenanceGroupTestMixin


class UsersEdit(LoginRequiredMixin, ManagerMaintenanceGroupTestMixin, View):
    """Update view for users app"""

    form_class: UserUpdateForm = UserUpdateForm
    template_name: str = "users/users_edit.html"

    def get_user(self, pk: int) -> User:
        return User.objects.get(pk=pk)

    def get(self, request: HttpRequest, pk: int) -> HttpResponse:
        return render(
            request,
            self.template_name,
            {"form": self.form_class(instance=self.get_user(pk))},
        )

    def post(self, request: HttpRequest, pk: int) -> HttpResponse:
        form: UserUpdateForm = self.form_class(request.POST, instance=self.get_user(pk))
        if form.is_valid():
            form.save()
            return redirect("users")
