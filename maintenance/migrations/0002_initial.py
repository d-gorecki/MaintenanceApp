# Generated by Django 4.1.1 on 2022-11-03 14:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("maintenance", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="maintenanceschedule",
            name="user",
            field=models.ForeignKey(
                help_text="Responsible",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="maintenancereport",
            name="schedule",
            field=models.OneToOneField(
                help_text="Corresponding maintenance schedule",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="maintenance.maintenanceschedule",
            ),
        ),
        migrations.AddField(
            model_name="maintenancereport",
            name="user",
            field=models.ForeignKey(
                help_text="Serviceman",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]