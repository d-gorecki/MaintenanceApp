from django import forms
from .models import MaintenanceType, MaintenanceSchedule
from machines.models import MachineGroup
from django.forms import Textarea, Select, DateInput


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


class MaintenanceScheduleForm(forms.ModelForm):
    class Meta:
        model = MaintenanceSchedule
        fields = ("machine", "maintenance_type", "planned_date", "user")
        widgets = {
            "machine": Select(attrs={"class": "form-select"}),
            "maintenance_type": Select(attrs={"class": "form-select"}),
            "user": Select(attrs={"class": "form-select"}),
            "planned_date": DateInput(attrs={"type": "date", "class": "form-control"}),
        }
