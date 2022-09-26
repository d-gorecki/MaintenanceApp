from django.contrib import admin
from django.urls import path
from .views import machines_comparison


urlpatterns = [
    path("", machines_comparison, name="machines_comparison"),
]
