# Generated by Django 4.1.1 on 2022-10-10 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("departments", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="department",
            name="name",
            field=models.CharField(help_text="Department name", max_length=32),
        ),
    ]