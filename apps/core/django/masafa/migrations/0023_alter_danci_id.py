# Generated by Django 4.2.5 on 2024-08-05 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('masafa', '0022_alter_danci_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='danci',
            name='id',
            field=models.CharField(default='#### {{charfield}}', max_length=255, primary_key=True, serialize=False),
        ),
    ]