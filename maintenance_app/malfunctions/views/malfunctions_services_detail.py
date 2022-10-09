from django.shortcuts import render
from django.views import View
from ..models import ServiceReport


class MalfunctionsServicesDetail(View):
    template_name = "malfunctions/malfunctions_services_detail.html"

    def get(self, request, pk):
        services_report = ServiceReport.objects.get(pk=pk)
        return render(request, self.template_name, {"services_report": services_report})
