# Generated by Django 5.0.1 on 2024-02-02 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purifier', '0024_remove_servicework_service_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='installed_product',
            field=models.ManyToManyField(blank=True, null=True, to='purifier.product'),
        ),
    ]
