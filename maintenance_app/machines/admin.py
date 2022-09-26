from django.contrib import admin
from .models import Machine

# Register your models here.


# class MachineAdmin(admin.ModelAdmin):
#     pass

admin.site.register(Machine)
