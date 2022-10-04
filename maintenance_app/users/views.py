from django.shortcuts import render


def users_profile(request):

    return render(request, "users/users_profile.html")
