# Generated by Django 4.2.5 on 2024-08-04 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('masafa', '0016_alter_danci_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='danci',
            name='id',
            field=models.CharField(default='######', max_length=255, primary_key=True, serialize=False),
        ),
    ]