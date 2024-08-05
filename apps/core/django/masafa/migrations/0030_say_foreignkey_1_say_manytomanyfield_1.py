# Generated by Django 4.2.5 on 2024-08-05 11:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('masafa', '0029_say_booleanfield_1_say_selectfield_1'),
    ]

    operations = [
        migrations.AddField(
            model_name='say',
            name='foreignkey_1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='masafa.danci', verbose_name='ForeignKey 1'),
        ),
        migrations.AddField(
            model_name='say',
            name='manytomanyfield_1',
            field=models.ManyToManyField(blank=True, null=True, to='masafa.cold', verbose_name='ManyToManyField 1'),
        ),
    ]