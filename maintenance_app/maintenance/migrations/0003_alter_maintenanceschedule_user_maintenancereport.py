# Generated by Django 4.1.1 on 2022-09-26 09:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("maintenance", "0002_maintenanceschedule"),
    ]

    operations = [
        migrations.AlterField(
            model_name="maintenanceschedule",
            name="user",
            field=models.ForeignKey(
                default=0,
                on_delete=django.db.models.deletion.SET_DEFAULT,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.CreateModel(
            name="MaintenanceReport",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date", models.DateTimeField(auto_now_add=True)),
                ("description", models.TextField()),
                ("image", models.FilePathField(path="/img")),
                (
                    "schedule",
                    models.ForeignKey(
                        default=0,
                        on_delete=django.db.models.deletion.SET_DEFAULT,
                        to="maintenance.maintenanceschedule",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        default=0,
                        on_delete=django.db.models.deletion.SET_DEFAULT,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]