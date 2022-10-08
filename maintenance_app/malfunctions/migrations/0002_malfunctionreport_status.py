# Generated by Django 4.1.1 on 2022-10-08 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("malfunctions", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="malfunctionreport",
            name="status",
            field=models.CharField(
                choices=[("pending", "pending"), ("finished", "finished")],
                default="pending",
                max_length=8,
            ),
        ),
    ]