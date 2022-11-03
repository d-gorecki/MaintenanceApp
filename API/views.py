from rest_framework import viewsets, permissions
from API.serializers import MachineSerializer
from machines.models.machine import Machine
from API.permissions import ManagerPermission


class MachineViewSet(viewsets.ModelViewSet):
    queryset = Machine.objects.all()
    serializer_class = MachineSerializer
    permission_classes = [ManagerPermission]
