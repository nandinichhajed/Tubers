# Generated by Django 3.2.9 on 2021-11-18 16:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('contactinfo', '0002_auto_20211117_1341'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactinfo',
            name='address',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contactinfo',
            name='area',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='contactinfo',
            name='country',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contactinfo',
            name='landmark',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='contactinfo',
            name='state',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contactinfo',
            name='town_or_city',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]
