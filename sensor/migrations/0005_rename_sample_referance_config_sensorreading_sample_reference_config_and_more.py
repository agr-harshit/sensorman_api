# Generated by Django 5.1.3 on 2024-12-13 11:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sensor', '0004_rename_sensor_calibration_date_sensorreading_calibration_date_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sensorreading',
            old_name='sample_referance_config',
            new_name='sample_reference_config',
        ),
        migrations.RenameField(
            model_name='sensorreading',
            old_name='sample_referance_monitor',
            new_name='sample_reference_monitor',
        ),
    ]
