# Generated by Django 4.2.5 on 2024-08-04 23:25

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('masafa', '0013_alter_danci_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='danci',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]