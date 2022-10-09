from django.shortcuts import render
from django.views import View
from ..models import MaintenanceType


class MaintenanceSchemes(View):
    template_name = "maintenance/maintenance_schemes.html"
    schemes = MaintenanceType.objects.all()

    def get(self, request):
        return render(request, self.template_name, {"schemes": self.schemes})
