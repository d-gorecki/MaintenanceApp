from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path("", views.machines, name="machines"),
    path("add/", views.machines_add, name="machines_add"),
    path("edit/<int:pk>/", views.machines_edit, name="machines_edit"),
]
