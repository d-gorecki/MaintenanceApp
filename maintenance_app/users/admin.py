from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            None,
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "department",
                    "group",
                    "email",
                    "function",
                    "mobile",
                )
            },
        ),
    )


admin.site.register(User, CustomUserAdmin)
