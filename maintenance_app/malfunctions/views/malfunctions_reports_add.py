from django.shortcuts import render, redirect
from django.views import View
from ..forms import ReportForm


class MalfunctionsReportsAdd(View):
    form_class = ReportForm
    template_name = "malfunctions/malfunctions_reports_add.html"

    def set_machine(self, request):
        machine = request.GET.get("machine")
        if machine:
            return self.form_class(initial={"machine": machine}, user=request.user)
        return self.form_class(user=request.user)

    def get(self, request):
        return render(request, self.template_name, {"form": self.set_machine(request)})

    def post(self, request):
        form = self.form_class(request.POST, request.FILES, user=request.user)
        if form.is_valid():
            report = form.save(commit=False)
            report.user = request.user
            report.save()
            return redirect("/malfunctions/pending/")
