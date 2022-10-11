from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from ..forms import ServiceReportForm
from maintenance_app.mixins import ManagerMaintenanceGroupTestMixin
from malfunctions.models.service_report import ServiceReport


class MalfunctionServicesAdd(
    LoginRequiredMixin, ManagerMaintenanceGroupTestMixin, View
):
    """Create view for malfunctions services (sub-module of malfunctions app)"""

    form_class: ServiceReportForm = ServiceReportForm
    template_name: str = "malfunctions/malfunctions_services_add.html"

    def get_malfunction(self, request: HttpRequest) -> ServiceReportForm:
        malfunction: int = request.GET.get("malfunction")
        if malfunction:
            return self.form_class(initial={"malfunction_report": malfunction})
        return self.form_class

    def get(self, request: HttpRequest) -> HttpResponse:
        return render(
            request, self.template_name, {"form": self.get_malfunction(request)}
        )

    def post(self, request: HttpRequest) -> HttpResponse:
        form: ServiceReportForm = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            report: ServiceReport = form.save(commit=False)
            report.user = request.user
            report.save()
            return redirect("/malfunctions/services")
