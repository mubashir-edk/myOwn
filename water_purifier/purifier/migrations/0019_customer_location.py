# Generated by Django 5.0.1 on 2024-01-05 00:47

import location_field.models.plain
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('purifier', '0018_remove_employee_district_remove_employee_state'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='location',
            field=location_field.models.plain.PlainLocationField(blank=True, max_length=63),
        ),
    ]