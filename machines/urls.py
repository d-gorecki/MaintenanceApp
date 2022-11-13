from django.urls import path

from .views import machines, machines_add, machines_edit

urlpatterns = [
    path("", machines.Machines.as_view(), name="machines"),
    path("add/", machines_add.MachinesAdd.as_view(), name="machines_add"),
    path("edit/<int:pk>/", machines_edit.MachinesEdit.as_view(), name="machines_edit"),
]
