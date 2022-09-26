from django.urls import path
from .views import malfunctions_pending


urlpatterns = [
    path("", malfunctions_pending, name="malfunctions_pending"),
]
