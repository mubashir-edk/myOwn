# Generated by Django 4.2.7 on 2023-12-01 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purifier', '0003_alter_category_image_alter_customer_customer_code_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='employee_code',
            field=models.CharField(blank=True, max_length=50, null=True, unique=True),
        ),
    ]
