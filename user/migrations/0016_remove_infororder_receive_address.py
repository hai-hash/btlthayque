# Generated by Django 3.1.7 on 2021-06-12 06:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0015_infororder_receive_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='infororder',
            name='receive_address',
        ),
    ]