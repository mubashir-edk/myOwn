# Generated by Django 4.2.7 on 2024-01-02 07:05

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('purifier', '0015_servicework_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceAssign',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('message', models.CharField(max_length=500)),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='purifier.servicework')),
                ('servicer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='purifier.servicer')),
            ],
        ),
    ]
