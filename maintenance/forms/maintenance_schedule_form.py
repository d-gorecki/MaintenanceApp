from typing import Any, Union

from django import forms
from django.forms import DateInput, Select

from maintenance.models.maintenance_schedule import MaintenanceSchedule


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
