# Generated by Django 3.1.7 on 2021-06-12 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0020_auto_20210612_1428'),
    ]

    operations = [
        migrations.AddField(
            model_name='shipment',
            name='name',
            field=models.CharField(default='', max_length=100),
        ),
    ]
