from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View
from ..forms import ServiceReportForm
from maintenance_app.mixins import ManagerMaintenanceGroupTestMixin


class MalfunctionServicesAdd(
    LoginRequiredMixin, ManagerMaintenanceGroupTestMixin, View
):
    form_class = ServiceReportForm
    template_name = "malfunctions/malfunctions_services_add.html"

    def get_malfunction(self, request):
        malfunction = request.GET.get("malfunction")
        if malfunction:
            return self.form_class(initial={"malfunction_report": malfunction})
        return self.form_class

    def get(self, request):
        return render(
            request, self.template_name, {"form": self.get_malfunction(request)}
        )

    def post(self, request):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            report = form.save(commit=False)
            report.user = request.user
            report.save()
            return redirect("/malfunctions/services")
