from django.test import TestCase
from maintenance.forms.maintenance_type_form import MaintenanceTypeForm
from maintenance.forms.maintenance_report_form import MaintenanceReportForm
from maintenance.forms.maintenance_schedule_form import MaintenanceScheduleForm


class TestMaintenanceForms(TestCase):
    def test_maintenance_type_form(self):
        form = MaintenanceTypeForm()
        fields = ["description", "machine_group", "type"]
        for field in fields:
            self.assertIn(field, form.fields)

    def test_maintenance_report_form(self):
        form = MaintenanceReportForm()
        fields = ["description", "schedule", "image"]
        for field in fields:
            self.assertIn(field, form.fields)

    def test_maintenance_schedule_form(self):
        form = MaintenanceScheduleForm()
        fields = ["machine", "maintenance_type", "planned_date", "user"]
        for field in fields:
            self.assertIn(field, form.fields)
