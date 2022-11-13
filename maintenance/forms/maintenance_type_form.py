from typing import Any, Union

from django import forms
from django.forms import Select, Textarea

from maintenance.models.maintenance_type import MaintenanceType


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
