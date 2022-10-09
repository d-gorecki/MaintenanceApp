from django.shortcuts import render
from django.views import View
from ..models import MalfunctionReport


class MalfunctionsReportsDetail(View):
    template_name = "malfunctions/malfunctions_reports_detail.html"

    def get(self, request, pk):
        malfunction_report = MalfunctionReport.objects.get(pk=pk)

        return render(
            request, self.template_name, {"malfunction_report": malfunction_report}
        )
