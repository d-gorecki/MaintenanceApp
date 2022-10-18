from django.urls import path, include
from API.views import (
    CRUDMachinesGroup,
    GetAllMachines,
    GetMachine,
    CreateMachine,
    UpdateMachine,
)

urlpatterns = [
    path("machines/", GetAllMachines.as_view(), name="get_machines"),
    path("machines/<int:pk>/", GetMachine.as_view(), name="get_machine"),
    path(
        "machine_groups/<int:pk>/",
        CRUDMachinesGroup.as_view(),
        name="get_machines_groups",
    ),
    path("machine/create/", CreateMachine.as_view(), name="create_machine"),
    path("machine/update/<int:pk>/", UpdateMachine.as_view(), name="update_machine"),
]
