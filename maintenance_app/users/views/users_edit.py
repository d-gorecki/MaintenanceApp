from django.shortcuts import render, redirect
from django.views import View
from ..forms import UserUpdateForm
from ..models import User


class UsersEdit(View):
    form_class = UserUpdateForm
    template_name = "users/users_edit.html"

    def get_user(self, pk):
        return User.objects.get(pk=pk)

    def get(self, request, pk):
        return render(
            request,
            self.template_name,
            {"form": self.form_class(instance=self.get_user(pk))},
        )

    def post(self, request, pk):
        form = self.form_class(request.POST, instance=self.get_user(pk))
        if form.is_valid():
            form.save()
            return redirect("users")
