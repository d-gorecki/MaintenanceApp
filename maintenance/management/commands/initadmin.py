from django.core.management.base import BaseCommand
from users.models import User


class Command(BaseCommand):
    """Management command to create default admin (superuser) during the first run of the app"""

    def handle(self, *args, **options) -> None:
        if not User.objects.count():
            User.objects.create_superuser(
                username="admin", password="admin", email="admin@admin.com"
            )
