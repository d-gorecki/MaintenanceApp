from typing import Any, OrderedDict

from rest_framework import serializers

from machines.models.machine import Machine


class MachineSerializer(serializers.ModelSerializer):
    class Meta:
        model: Machine = Machine
        fields: list[str] = [
            "factory_number",
            "machine_group",
            "name",
            "number",
            "producer",
            "purchase_data",
            "department",
            "machine_status",
        ]

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
