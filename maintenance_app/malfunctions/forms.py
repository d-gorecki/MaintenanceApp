from django import forms
from machines.models import Machine
from .models import MalfunctionReport, ServiceReport


class ReportForm(forms.ModelForm):
    def __init__(self, *args, user=None, **kwargs):
        super(ReportForm, self).__init__(*args, **kwargs)
        if user.group == "production":
            self.fields["machine"].queryset = Machine.objects.filter(
                department=user.department
            )

    image = forms.ImageField(required=False)

    class Meta:
        model = MalfunctionReport
        fields = ("machine", "description", "image")
        widgets = {
            "machine": forms.Select(attrs={"class": "form-select"}),
            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Malfunction description",
                }
            ),
        }


class ServiceReportForm(forms.ModelForm):
    image = forms.ImageField(required=False)

    class Meta:
        model = ServiceReport
        fields = ("malfunction_report", "description", "image")
        widgets = {
            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Malfunction description",
                }
            ),
            "malfunction_report": forms.Select(attrs={"class": "form-select"}),
        }
