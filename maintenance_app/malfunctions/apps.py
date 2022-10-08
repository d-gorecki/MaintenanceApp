from django.apps import AppConfig


class MalfunctionsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "malfunctions"

    def ready(self):
        import malfunctions.signals
