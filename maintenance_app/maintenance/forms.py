from django import forms
from .models import MaintenanceType
from machines.models import MachineGroup


class MaintenanceTypeForm(forms.ModelForm):
    class Meta:
        model = MaintenanceType
        fields = "__all__"
