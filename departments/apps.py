from django.apps import AppConfig


class DepartmentsConfig(AppConfig):
    default_auto_field: str = "django.db.models.BigAutoField"
    name: str = "departments"
