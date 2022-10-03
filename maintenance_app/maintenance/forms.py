from django import forms
from .models import MaintenanceType
from machines.models import MachineGroup
from django.forms import Textarea, Select


class MaintenanceTypeForm(forms.ModelForm):
    class Meta:
        model = MaintenanceType
        fields = ("type", "machine_group", "description")
        widgets = {
            "description": Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Malfunction description",
                }
            ),
            "machine_group": Select(attrs={"class": "form-select"}),
            "type": Select(attrs={"class": "form-select"}),
        }
