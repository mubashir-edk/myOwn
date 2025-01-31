# Generated by Django 4.2.7 on 2023-12-14 04:55

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('purifier', '0008_alter_customer_address_alter_customer_mobile_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('test_name', models.CharField(max_length=150)),
                ('ph_value', models.CharField(max_length=30)),
                ('tds_value', models.CharField(max_length=30)),
                ('iron_value', models.CharField(max_length=30)),
                ('hardness_value', models.CharField(max_length=30)),
                ('turbuet_value', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='ServiceWork',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('comment_section', models.TextField()),
                ('service_date', models.DateField()),
                ('remark_section', models.TextField()),
                ('customer_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='purifier.customer')),
                ('service_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='purifier.service')),
            ],
        ),
    ]
