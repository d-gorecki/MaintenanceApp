from django.shortcuts import render, redirect
from django.views import View
from ..forms import MaintenanceTypeForm


class MaintenanceSchemesAdd(View):
    form_class = MaintenanceTypeForm
    template_name = "maintenance/maintenance_schemes_add.html"

    def get(self, request):
        return render(request, self.template_name, {"form": self.form_class()})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/maintenance/")
