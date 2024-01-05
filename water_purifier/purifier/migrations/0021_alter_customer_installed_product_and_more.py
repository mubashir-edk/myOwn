# Generated by Django 5.0.1 on 2024-01-05 05:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purifier', '0020_remove_customer_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='installed_product',
            field=models.ManyToManyField(to='purifier.product'),
        ),
        migrations.AlterField(
            model_name='serviceassign',
            name='servicer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='purifier.servicer'),
        ),
    ]
