# Generated by Django 4.2.5 on 2025-03-16 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("frappe_app", "0004_alter_systemsettings_reset_password_link_expiry_duration"),
    ]

    operations = [
        migrations.AlterField(
            model_name="systemsettings",
            name="reset_password_link_expiry_duration",
            field=models.DurationField(blank=True, null=True),
        ),
    ]
