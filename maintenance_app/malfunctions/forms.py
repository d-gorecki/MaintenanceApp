from django import forms
from machines.models import Machine


class ReportForm(forms.Form):
    machine = forms.ModelChoiceField(
        queryset=Machine.objects.all(), help_text="Machine"
    )
    description = forms.CharField(
        widget=forms.Textarea(
            attrs={"class": "form-control", "placeholder": "Malfunction description"}
        )
    )
    image = forms.ImageField(required=False)
