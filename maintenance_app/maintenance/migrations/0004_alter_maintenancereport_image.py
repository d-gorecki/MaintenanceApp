# Generated by Django 4.1.1 on 2022-09-26 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("maintenance", "0003_alter_maintenanceschedule_user_maintenancereport"),
    ]

    operations = [
        migrations.AlterField(
            model_name="maintenancereport",
            name="image",
            field=models.ImageField(upload_to="media/"),
        ),
    ]