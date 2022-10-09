from django.views.generic import ListView
from ..models import MalfunctionReport


class MalfunctionsReports(ListView):
    model = MalfunctionReport
    template_name = "malfunctions/malfunctions_reports.html"
    ordering = ["-id"]
    context_object_name = "malfunction_reports"
