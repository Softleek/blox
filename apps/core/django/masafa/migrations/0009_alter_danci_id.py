# Generated by Django 4.2.5 on 2024-08-04 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('masafa', '0008_alter_danci_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='danci',
            name='id',
            field=models.CharField(default='000001', max_length=6, primary_key=True, serialize=False),
        ),
    ]