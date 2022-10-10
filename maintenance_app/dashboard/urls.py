from django.urls import path
from . import views
from typing import Callable

urlpatterns: list[Callable] = [
    path("", views.Dashboard.as_view(), name="dashboard"),
]
