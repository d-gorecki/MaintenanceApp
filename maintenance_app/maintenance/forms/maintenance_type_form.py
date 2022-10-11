from typing import Union, Any
from django import forms
from maintenance.models.maintenance_type import MaintenanceType
from django.forms import Textarea, Select


class MaintenanceTypeForm(forms.ModelForm):
    class Meta:
        model: MaintenanceType = MaintenanceType
        fields: tuple[str] = ("type", "machine_group", "description")
        widgets: dict[str, Union[Textarea, Select, Any]] = {
            "description": Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Malfunction description",
                }
            ),
            "machine_group": Select(attrs={"class": "form-select"}),
            "type": Select(attrs={"class": "form-select"}),
        }
