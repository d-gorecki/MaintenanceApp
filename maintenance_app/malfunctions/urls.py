from django.urls import path
from . import views


urlpatterns = [
    path("pending/", views.malfunctions_pending, name="malfunctions_pending"),
    path("reports/", views.malfunctions_reports, name="malfunctions_reports"),
    path(
        "reports/add/", views.malfunctions_reports_add, name="malfunctions_reports_add"
    ),
    path(
        "reports/<int:pk>",
        views.malfunctions_reports_detail,
        name="malfunctions_reports_detail",
    ),
]
