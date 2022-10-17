from django.test import TestCase
from machines.forms import MachineAddForm


class TestMachineAddForm(TestCase):
    def test_machine_add_form(self):
        form = MachineAddForm()
        self.assertIn("factory_number", form.fields)
        self.assertIn("producer", form.fields)
        self.assertIn("machine_group", form.fields)
        self.assertIn("department", form.fields)
        self.assertIn("purchase_data", form.fields)
        self.assertIn("number", form.fields)
