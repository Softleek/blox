# Generated by Django 4.2.5 on 2024-08-05 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('masafa', '0027_alter_cold_emailfield_1'),
    ]

    operations = [
        migrations.CreateModel(
            name='Say',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('id', models.CharField(default='000000', max_length=6, primary_key=True, serialize=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]