from typing import Union, Any

from django import forms
from maintenance.models.maintenance_type import MaintenanceType
from maintenance.models.maintenance_schedule import MaintenanceSchedule
from maintenance.models.maintenance_report import MaintenanceReport

from django.forms import Textarea, Select, DateInput


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


class MaintenanceReportForm(forms.ModelForm):
    class Meta:
        model: MaintenanceReport = MaintenanceReport
        fields: tuple[str] = ("schedule", "description", "image")
        widgets: dict[str, Union[Select, Textarea]] = {
            "schedule": Select(attrs={"class": "form-select"}),
            "description": Textarea(attrs={"class": "form-control"}),
        }
