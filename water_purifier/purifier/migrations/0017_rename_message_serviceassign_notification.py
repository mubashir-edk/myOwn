# Generated by Django 4.2.7 on 2024-01-03 13:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('purifier', '0016_serviceassign'),
    ]

    operations = [
        migrations.RenameField(
            model_name='serviceassign',
            old_name='message',
            new_name='notification',
        ),
    ]
