# Generated by Django 5.0.1 on 2024-01-09 09:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purifier', '0022_alter_serviceassign_notification_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicework',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('working', 'Working'), ('completed', 'Completed')], default=124124, max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='serviceassign',
            name='servicer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='purifier.servicer'),
        ),
    ]
