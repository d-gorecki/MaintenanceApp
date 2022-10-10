from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from ..forms import ReportForm
from ..models import MalfunctionReport


class MalfunctionsReportsAdd(View):
    """Create view for malfunctions reports (sub-module of malfunctions app)"""

    form_class: ReportForm = ReportForm
    template_name: str = "malfunctions/malfunctions_reports_add.html"

    def set_machine(self, request: HttpRequest) -> ReportForm:
        machine: int = request.GET.get("machine")
        if machine:
            return self.form_class(initial={"machine": machine}, user=request.user)
        return self.form_class(user=request.user)

    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, self.template_name, {"form": self.set_machine(request)})

    def post(self, request: HttpRequest) -> HttpResponse:
        form = self.form_class(request.POST, request.FILES, user=request.user)
        if form.is_valid():
            report: MalfunctionReport = form.save(commit=False)
            report.user = request.user
            report.save()
            return redirect("/malfunctions/pending/")
