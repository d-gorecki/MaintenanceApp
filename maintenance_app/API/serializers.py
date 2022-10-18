from typing import OrderedDict, Any

from rest_framework import serializers
from machines.models.machine import Machine
from machines.models.machine_group import MachineGroup


class MachineSerializer(serializers.ModelSerializer):
    class Meta:
        model: Machine = Machine
        fields: str = "__all__"

    def to_representation(self, instance) -> OrderedDict[Any, Any | None]:
        representation: OrderedDict[Any, Any | None] = super().to_representation(
            instance
        )
        purchase_date: Any = instance.purchase_data
        if purchase_date:
            representation["purchase_data"] = instance.purchase_data.strftime(
                "%d-%m-%Y"
            )
        return representation


class MachineGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = MachineGroup
        fields = "__all__"
