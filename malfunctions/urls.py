from django.urls import path

from .views import (malfunctions_pending, malfunctions_reports,
                    malfunctions_reports_add, malfunctions_reports_detail,
                    malfunctions_services, malfunctions_services_add,
                    malfunctions_services_detail)

urlpatterns = [
    path(
        "pending/",
        malfunctions_pending.MalfunctionsPending.as_view(),
        name="malfunctions_pending",
    ),
    path(
        "reports/",
        malfunctions_reports.MalfunctionsReports.as_view(),
        name="malfunctions_reports",
    ),
    path(
        "reports/add/",
        malfunctions_reports_add.MalfunctionsReportsAdd.as_view(),
        name="malfunctions_reports_add",
    ),
    path(
        "reports/<int:pk>",
        malfunctions_reports_detail.MalfunctionsReportsDetail.as_view(),
        name="malfunctions_reports_detail",
    ),
    path(
        "services/",
        malfunctions_services.MalfunctionsServices.as_view(),
        name="malfunctions_services",
    ),
    path(
        "services/<int:pk>",
        malfunctions_services_detail.MalfunctionsServicesDetail.as_view(),
        name="malfunctions_services_detail",
    ),
    path(
        "services/add",
        malfunctions_services_add.MalfunctionServicesAdd.as_view(),
        name="malfunctions_services_add",
    ),
]
