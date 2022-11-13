from typing import Any, Union

from django import forms
from django.forms import Select, Textarea

from malfunctions.models.malfunction_report import MalfunctionReport
from malfunctions.models.service_report import ServiceReport


class ServiceReportForm(forms.ModelForm):
    def __init__(self, *args, **kwargs) -> None:
        super(ServiceReportForm, self).__init__(*args, **kwargs)
        self.fields["malfunction_report"].queryset = MalfunctionReport.objects.filter(
            status="pending"
        )

    image = forms.ImageField(required=False)

    class Meta:
        model: ServiceReport = ServiceReport
        fields: tuple[str] = ("malfunction_report", "description", "image", "service")
        widgets: dict[str, Union[Textarea, Select, Any]] = {
            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Malfunction description",
                }
            ),
            "malfunction_report": forms.Select(attrs={"class": "form-select"}),
            "service": forms.Select(attrs={"class": "form-select"}),
        }
