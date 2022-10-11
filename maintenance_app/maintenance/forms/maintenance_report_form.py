from typing import Union
from django import forms
from maintenance.models.maintenance_report import MaintenanceReport
from django.forms import Textarea, Select


class MaintenanceReportForm(forms.ModelForm):
    class Meta:
        model: MaintenanceReport = MaintenanceReport
        fields: tuple[str] = ("schedule", "description", "image")
        widgets: dict[str, Union[Select, Textarea]] = {
            "schedule": Select(attrs={"class": "form-select"}),
            "description": Textarea(attrs={"class": "form-control"}),
        }
