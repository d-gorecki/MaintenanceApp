from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path("", views.machines_comparison, name="machines_comparison"),
]
