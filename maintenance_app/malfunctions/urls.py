from django.urls import path
from .views import malfunctions_pending, malfunctions_report


urlpatterns = [
    path("pending/", malfunctions_pending, name="malfunctions_pending"),
    path("report/", malfunctions_report, name="malfunctions_report"),
]
