# Generated by Django 4.1.1 on 2022-11-03 14:31

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("machines", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("malfunctions", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="servicereport",
            name="user",
            field=models.ForeignKey(
                default=0,
                help_text="Serviceman",
                on_delete=django.db.models.deletion.SET_DEFAULT,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="malfunctionreport",
            name="machine",
            field=models.ForeignKey(
                help_text="Machine",
                on_delete=django.db.models.deletion.CASCADE,
                to="machines.machine",
            ),
        ),
        migrations.AddField(
            model_name="malfunctionreport",
            name="user",
            field=models.ForeignKey(
                default=0,
                help_text="Reporting user",
                on_delete=django.db.models.deletion.SET_DEFAULT,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
