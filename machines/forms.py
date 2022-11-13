from typing import Union

from django import forms
from django.forms import DateInput, Select, TextInput

from machines.models.machine import Machine


class MachineAddForm(forms.ModelForm):
    class Meta:
        model: Machine = Machine
        fields: str = "__all__"

        widgets: dict[str, Union[TextInput, Select]] = {
            "factory_number": TextInput(attrs={"class": "form-control"}),
            "name": TextInput(attrs={"class": "form-control"}),
            "producer": TextInput(attrs={"class": "form-control"}),
            "machine_group": Select(attrs={"class": "form-select"}),
            "machine_status": Select(attrs={"class": "form-select"}),
            "department": Select(attrs={"class": "form-select"}),
            "purchase_data": DateInput(attrs={"type": "date", "class": "form-control"}),
            "number": TextInput(attrs={"class": "form-control"}),
        }
