from pyexpat.errors import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View
from ..forms import ManagerUserCreationForm


class UsersAdd(LoginRequiredMixin, View):
    form_class = ManagerUserCreationForm
    template_name = "users/users_add.html"

    def get(self, request):
        return render(request, self.template_name, {"form": self.form_class()})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            messages.success(
                request, f"Account created successfully for user {username}"
            )
            return redirect("users_profile")
