from django.urls import path, include
from . import views


urlpatterns = [
    path("", views.maintenance_schemes, name="maintenance_schemes"),
    path("schemes/", views.maintenance_schemes, name="maintenance_schemes"),
    path(
        "schemes/<int:pk>",
        views.maintanance_schemes_detail,
        name="maintenance_schemes_detail",
    ),
    path(
        "schemes/machine_group/<int:pk>",
        views.maintenacne_schemes_group,
        name="maintenance_schemes_group",
    ),
    path(
        "schemes/type/<slug:type>",
        views.maintenacne_schemes_type,
        name="maintenance_schemes_type",
    ),
]
