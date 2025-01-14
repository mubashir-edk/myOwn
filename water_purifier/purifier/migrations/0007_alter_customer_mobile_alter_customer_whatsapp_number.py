# Generated by Django 4.2.7 on 2023-12-05 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purifier', '0006_customer_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='mobile',
            field=models.CharField(help_text='Mobile number', max_length=20),
        ),
        migrations.AlterField(
            model_name='customer',
            name='whatsapp_number',
            field=models.CharField(help_text='Whatsapp number', max_length=20),
        ),
    ]
