from pyexpat.errors import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from ..forms import ManagerUserCreationForm
from maintenance_app.mixins import ManagerMaintenanceGroupTestMixin


class UsersAdd(LoginRequiredMixin, ManagerMaintenanceGroupTestMixin, View):
    """Create view for users app"""

    form_class: ManagerUserCreationForm = ManagerUserCreationForm
    template_name: str = "users/users_add.html"

    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, self.template_name, {"form": self.form_class()})

    def post(self, request: HttpRequest) -> HttpResponse:
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            username: str = form.cleaned_data["username"]
            messages.success(
                request, f"Account created successfully for user {username}"
            )
            return redirect("users_profile")
