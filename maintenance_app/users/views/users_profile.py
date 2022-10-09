from pyexpat.errors import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View


class UsersProfile(LoginRequiredMixin, View):
    form_class = PasswordChangeForm
    template_name = "users/users_profile.html"

    def get(self, request):
        return render(
            request, self.template_name, {"form": self.form_class(user=request.user)}
        )

    def post(self, request):
        form = self.form_class(request.user, request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, f"Password has been changed for account {request.user}"
            )
            return redirect("users_login")
