from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm
from .forms import ManagerUserCreationForm
from django.contrib import messages
from django.shortcuts import HttpResponse


@login_required()
def users_profile(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, f"Password has been changed for account {request.user}"
            )
            return redirect("users_login")

    form = PasswordChangeForm(user=request.user)
    context = {"form": form}

    return render(request, "users/users_profile.html", context)


def users_add(request):
    if request.method == "POST":
        form = ManagerUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            messages.success(
                request, f"Account created successfully for user {username}"
            )
            return redirect("users_profile")

    form = ManagerUserCreationForm()
    context = {"form": form}

    return render(request, "users/users_add.html", context)
