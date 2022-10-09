from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View

from ..models import MalfunctionReport
from maintenance_app.mixins import ManagerMaintenanceGroupTestMixin


class MalfunctionsPending(LoginRequiredMixin, ManagerMaintenanceGroupTestMixin, View):
    template_name = "malfunctions/malfunctions_pending.html"

    def get(self, request):
        malfunctions = MalfunctionReport.objects.filter(status="pending")
        return render(request, self.template_name, {"malfunctions": malfunctions})
