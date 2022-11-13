from typing import Union

from django import forms
from django.forms import Select, Textarea

from maintenance.models.maintenance_report import MaintenanceReport
from maintenance.models.maintenance_schedule import MaintenanceSchedule


class MaintenanceReportForm(forms.ModelForm):
    def __init__(self, *args, **kwargs) -> None:
        super(MaintenanceReportForm, self).__init__(*args, **kwargs)
        self.fields["schedule"].queryset = MaintenanceSchedule.objects.filter(
            status="pending"
        )

    image = forms.ImageField(required=False)

    class Meta:
        model: MaintenanceReport = MaintenanceReport
        fields: tuple[str] = ("schedule", "description", "image")
        widgets: dict[str, Union[Select, Textarea]] = {
            "schedule": Select(attrs={"class": "form-select"}),
            "description": Textarea(attrs={"class": "form-control"}),
        }
