from django.urls import path, include
from . import views


urlpatterns = [
    path("", views.maintenance_schemes, name="maintenance_schemes"),
    path("schemes/", views.maintenance_schemes, name="maintenance_schemes"),
    path(
        "schemes/<int:pk>",
        views.maintenance_schemes_detail,
        name="maintenance_schemes_detail",
    ),
    path(
        "schemes/machine_group/<int:pk>",
        views.maintenance_schemes_group,
        name="maintenance_schemes_group",
    ),
    path(
        "schemes/type/<slug:type>",
        views.maintenance_schemes_type,
        name="maintenance_schemes_type",
    ),
    path("schemes/add/", views.maintenance_schemes_add, name="maintenance_schemes_add"),
    path(
        "schemes/edit/<int:pk>",
        views.maintenance_schemes_edit,
        name="maintenance_schemes_edit",
    ),
    path("schedules/", views.maintenance_schedules, name="maintenance_schedules"),
    path(
        "schedules/add/",
        views.maintenance_schedules_add,
        name="maintenance_schedules_add",
    ),
    path(
        "schedules/edit/<int:pk>",
        views.maintenance_schedules_edit,
        name="maintenance_schedules_edit",
    ),
    path("schedules/reports/", views.maintenance_reports, name="maintenance_reports"),
    path(
        "schedules/reports/<int:pk>",
        views.maintenance_reports_detail,
        name="maintenance_reports_detail",
    ),
]
