from django.contrib import admin
from .models import MalfunctionReport, MalfunctionPending, ServiceReport

admin.site.register(MalfunctionReport)
admin.site.register(MalfunctionPending)
admin.site.register(ServiceReport)
