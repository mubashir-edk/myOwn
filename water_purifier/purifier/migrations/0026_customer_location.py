# Generated by Django 4.2.9 on 2024-02-07 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purifier', '0025_alter_customer_installed_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='location',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
