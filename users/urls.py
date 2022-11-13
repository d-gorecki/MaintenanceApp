from django.contrib.auth import views as auth_views
from django.urls import path

from .views import users, users_add, users_edit, users_profile

urlpatterns = [
    path("", users.Users.as_view(), name="users"),
    path("edit/<int:pk>/", users_edit.UsersEdit.as_view(), name="users_edit"),
    path("profile/", users_profile.UsersProfile.as_view(), name="users_profile"),
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
    path("add/", users_add.UsersAdd.as_view(), name="users_add"),
]
