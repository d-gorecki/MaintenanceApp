from django.shortcuts import render
from django.views import View
from ..models import ServiceReport


class MalfunctionsServices(View):
    template_name = "malfunctions/malfunctions_services.html"

    def get(self, request):
        services = ServiceReport.objects.all()
        return render(request, self.template_name, {"services": services})
