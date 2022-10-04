from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("profile/", views.users_profile, name="users_profile"),
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="users/users_login.html"),
        name="users_login",
    ),
    path(
        "logout/",
        auth_views.LogoutView.as_view(template_name="users/users_logout.html"),
        name="users_logout",
    ),
]
