# Generated by Django 4.1.1 on 2022-09-26 08:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("machines", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="MaintenanceType",
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
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("week", "weekly maintenance"),
                            ("month", "monthly maintenance"),
                            ("half year", "half year maintenance"),
                            ("year", "annual maintenance"),
                            ("two years", "two years maintenacne"),
                            ("three years", "three years maintenance"),
                            ("additional", "non-standard maintenacne"),
                        ],
                        default="week",
                        max_length=50,
                    ),
                ),
                ("description", models.TextField()),
                (
                    "machine_group",
                    models.ForeignKey(
                        default=0,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="machines.machinegroup",
                    ),
                ),
            ],
        ),
    ]
