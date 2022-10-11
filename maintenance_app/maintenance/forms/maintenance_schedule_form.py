from typing import Union, Any
from django import forms
from maintenance.models.maintenance_schedule import MaintenanceSchedule
from django.forms import Select, DateInput


class MaintenanceScheduleForm(forms.ModelForm):
    class Meta:
        model: MaintenanceSchedule = MaintenanceSchedule
        fields: tuple[str] = ("machine", "maintenance_type", "planned_date", "user")
        widgets: dict[str, Union[Select, DateInput, Any]] = {
            "machine": Select(attrs={"class": "form-select"}),
            "maintenance_type": Select(attrs={"class": "form-select"}),
            "user": Select(attrs={"class": "form-select"}),
            "planned_date": DateInput(attrs={"type": "date", "class": "form-control"}),
        }
