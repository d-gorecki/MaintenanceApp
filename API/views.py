from rest_framework import permissions, viewsets

from API.permissions import ManagerPermission
from API.serializers import MachineSerializer
from machines.models.machine import Machine


class MachineViewSet(viewsets.ModelViewSet):
    queryset = Machine.objects.all()
    serializer_class = MachineSerializer
    permission_classes = [ManagerPermission]
