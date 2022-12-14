from django.urls import path

from .views import (maintenance_reports, maintenance_reports_add,
                    maintenance_reports_detail, maintenance_schedules,
                    maintenance_schedules_add, maintenance_schedules_edit,
                    maintenance_schemes, maintenance_schemes_add,
                    maintenance_schemes_detail, maintenance_schemes_edit,
                    maintenance_schemes_group, maintenance_schemes_type)

urlpatterns = [
    path(
        "", maintenance_schemes.MaintenanceSchemes.as_view(), name="maintenance_schemes"
    ),
    path(
        "schemes/",
        maintenance_schemes.MaintenanceSchemes.as_view(),
        name="maintenance_schemes",
    ),
    path(
        "schemes/<int:pk>",
        maintenance_schemes_detail.MaintenanceSchemesDetail.as_view(),
        name="maintenance_schemes_detail",
    ),
    path(
        "schemes/machine_group/<int:pk>",
        maintenance_schemes_group.MaintenanceSchemesGroup.as_view(),
        name="maintenance_schemes_group",
    ),
    path(
        "schemes/type/<slug:type>",
        maintenance_schemes_type.MaintenanceSchemesType.as_view(),
        name="maintenance_schemes_type",
    ),
    path(
        "schemes/add/",
        maintenance_schemes_add.MaintenanceSchemesAdd.as_view(),
        name="maintenance_schemes_add",
    ),
    path(
        "schemes/edit/<int:pk>",
        maintenance_schemes_edit.MaintenanceSchemesEdit.as_view(),
        name="maintenance_schemes_edit",
    ),
    path(
        "schedules/",
        maintenance_schedules.MaintenanceSchedules.as_view(),
        name="maintenance_schedules",
    ),
    path(
        "schedules/add/",
        maintenance_schedules_add.MaintenanceSchedulesAdd.as_view(),
        name="maintenance_schedules_add",
    ),
    path(
        "schedules/edit/<int:pk>",
        maintenance_schedules_edit.MaintenanceSchedulesEdit.as_view(),
        name="maintenance_schedules_edit",
    ),
    path(
        "schedules/reports/",
        maintenance_reports.MaintenanceReports.as_view(),
        name="maintenance_reports",
    ),
    path(
        "schedules/reports/<int:pk>",
        maintenance_reports_detail.MaintenanceReportsDetail.as_view(),
        name="maintenance_reports_detail",
    ),
    path(
        "schedules/reports/add",
        maintenance_reports_add.MaintenanceReportsAdd.as_view(),
        name="maintenance_reports_add",
    ),
]
