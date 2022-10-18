from django.db.models import QuerySet
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import generics
from API.serializers import MachineSerializer, MachineGroupSerializer
from machines.models.machine import Machine
from machines.models.machine_group import MachineGroup
from API.permissions import ManagerPermission


class GetAllMachines(generics.ListAPIView):
    serializer_class: MachineSerializer = MachineSerializer
    queryset: QuerySet[Machine] = Machine.objects.all()
    permission_classes = [IsAuthenticated]


class GetMachine(generics.RetrieveAPIView):
    serializer_class: MachineSerializer = MachineSerializer
    queryset: Machine = Machine
    permission_classes = [IsAuthenticated]


class CreateMachine(generics.CreateAPIView):
    serializer_class: MachineSerializer = MachineSerializer
    permission_classes = [IsAuthenticated, ManagerPermission]


class UpdateMachine(generics.RetrieveUpdateAPIView):
    serializer_class: MachineSerializer = MachineSerializer
    queryset: Machine = Machine
    permission_classes = [IsAuthenticated, ManagerPermission]


class CRUDMachinesGroup(generics.RetrieveUpdateDestroyAPIView):
    serializer_class: MachineGroupSerializer = MachineGroupSerializer
    queryset: QuerySet[MachineGroup] = MachineGroup
    permission_classes = [IsAuthenticated, ManagerPermission]
