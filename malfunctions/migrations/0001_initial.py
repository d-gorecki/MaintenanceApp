# Generated by Django 4.1.1 on 2022-11-03 14:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="MalfunctionReport",
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
                ("datetime", models.DateTimeField(auto_now_add=True)),
                ("description", models.TextField(help_text="Description")),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        help_text="Allowed format (.jpg, .png)",
                        upload_to="media/malfunction_issues",
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[("pending", "pending"), ("finished", "finished")],
                        default="pending",
                        help_text="Machine status",
                        max_length=8,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ServiceReport",
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
                ("datetime", models.DateTimeField(auto_now_add=True)),
                ("description", models.TextField(help_text="Description")),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        help_text="Allowed formats (.png, .jpg)",
                        upload_to="media/service_reports",
                    ),
                ),
                (
                    "service",
                    models.CharField(
                        choices=[("pending", "pending"), ("finished", "finished")],
                        default="pending",
                        help_text="Status after service",
                        max_length=8,
                    ),
                ),
                (
                    "malfunction_report",
                    models.ForeignKey(
                        default=0,
                        help_text="Corresponding malfunction report",
                        on_delete=django.db.models.deletion.SET_DEFAULT,
                        to="malfunctions.malfunctionreport",
                    ),
                ),
            ],
        ),
    ]