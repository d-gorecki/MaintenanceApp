from django.shortcuts import render


def maintenance_main_view(request):
    return render(request, "maintenance/base.html")
