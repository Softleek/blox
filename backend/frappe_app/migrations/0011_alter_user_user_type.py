# Generated by Django 4.2.5 on 2025-03-16 21:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("frappe_app", "0010_rename_new_password_user_password"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="user_type",
            field=models.ForeignKey(
                blank=True,
                default="",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="UserUserType",
                to="frappe_app.usertype",
            ),
        ),
    ]
