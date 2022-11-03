from django.test import TestCase
from malfunctions.forms.report_form import ReportForm
from malfunctions.forms.service_report_form import ServiceReportForm
from dashboard.tests import UserTestUtils
from malfunctions.tests.test_models import MalfunctionTestUtils


class TestMalfunctionForms(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = UserTestUtils.create_user()
        MalfunctionTestUtils.create_malfunction_report(user=cls.user)

    def test_report_form(self):
        form = ReportForm(user=self.user)
        fields = ["machine", "description", "image"]
        for field in fields:
            self.assertIn(field, form.fields)

    def test_service_report(self):
        form = ServiceReportForm()
        fields = ["malfunction_report", "description", "image", "service"]
        for field in fields:
            self.assertIn(field, form.fields)
