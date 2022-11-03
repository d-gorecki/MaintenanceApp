from django.apps import AppConfig


class MachinesConfig(AppConfig):
    default_auto_field: str = "django.db.models.BigAutoField"
    name: str = "machines"

    def ready(self):
        from . import signals
