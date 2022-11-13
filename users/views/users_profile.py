from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.views import View
from pyexpat.errors import messages


class UsersProfile(LoginRequiredMixin, View):
    """Update(self) view for users app"""

    form_class: PasswordChangeForm = PasswordChangeForm
    template_name: str = "users/users_profile.html"

    def get(self, request: HttpRequest) -> HttpResponse:
        return render(
            request, self.template_name, {"form": self.form_class(user=request.user)}
        )

    def post(self, request: HttpRequest) -> HttpResponse:
        form = self.form_class(request.user, request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, f"Password has been changed for account {request.user}"
            )
            return redirect("users_login")
