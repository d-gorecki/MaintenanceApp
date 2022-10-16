# Generated by Django 4.1.1 on 2022-10-10 14:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("departments", "0002_alter_department_name"),
        ("machines", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="machine",
            name="department",
            field=models.ForeignKey(
                help_text="Department",
                on_delete=django.db.models.deletion.CASCADE,
                to="departments.department",
            ),
        ),
        migrations.AlterField(
            model_name="machine",
            name="factory_number",
            field=models.CharField(help_text="Factory number", max_length=100),
        ),
        migrations.AlterField(
            model_name="machine",
            name="machine_group",
            field=models.ForeignKey(
                default=0,
                help_text="Machine group",
                on_delete=django.db.models.deletion.CASCADE,
                to="machines.machinegroup",
            ),
        ),
        migrations.AlterField(
            model_name="machine",
            name="machine_status",
            field=models.CharField(
                choices=[
                    ("available", "working fine"),
                    ("nonwork", "not working"),
                    ("attention", "need some repairs but working"),
                ],
                default="available",
                help_text="Machine status (available/not working)",
                max_length=32,
            ),
        ),
        migrations.AlterField(
            model_name="machine",
            name="name",
            field=models.CharField(help_text="Machine name(model)", max_length=100),
        ),
        migrations.AlterField(
            model_name="machine",
            name="number",
            field=models.CharField(help_text="Department number", max_length=100),
        ),
        migrations.AlterField(
            model_name="machine",
            name="producer",
            field=models.CharField(help_text="Producer", max_length=100),
        ),
        migrations.AlterField(
            model_name="machine",
            name="purchase_data",
            field=models.DateField(blank=True, help_text="Purchase date"),
        ),
        migrations.AlterField(
            model_name="machinegroup",
            name="name",
            field=models.CharField(help_text="Machine group", max_length=100),
        ),
    ]