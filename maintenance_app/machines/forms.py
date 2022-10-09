from django import forms
from django.forms import Select, DateInput, TextInput

from .models import Machine


class MachineAddForm(forms.ModelForm):
    class Meta:
        model = Machine
        fields = "__all__"

        widgets = {
            "factory_number": TextInput(attrs={"class": "form-control"}),
            "producer": TextInput(attrs={"class": "form-control"}),
            "machine_group": Select(attrs={"class": "form-select"}),
            "machine_status": Select(attrs={"class": "form-select"}),
            "department": Select(attrs={"class": "form-select"}),
            "purchase_data": DateInput(attrs={"type": "date", "class": "form-control"}),
            "number": TextInput(attrs={"class": "form-control"}),
        }
