from typing import Any, Union

from django import forms
from django.forms import Select, Textarea
from machines.models import Machine
from .models import MalfunctionReport, ServiceReport
from users.models import User


class ReportForm(forms.ModelForm):
    def __init__(self, *args, user: User = None, **kwargs) -> None:
        super(ReportForm, self).__init__(*args, **kwargs)
        if user.group == "production":
            self.fields["machine"].queryset = Machine.objects.filter(
                department=user.department
            )

    image = forms.ImageField(required=False)

    class Meta:
        model: MalfunctionReport = MalfunctionReport
        fields: tuple[str] = ("machine", "description", "image")
        widgets: dict[str, Union[Select, Textarea, Any]] = {
            "machine": forms.Select(attrs={"class": "form-select"}),
            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Malfunction description",
                }
            ),
        }


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
