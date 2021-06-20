# Generated by Django 3.1.7 on 2021-06-12 04:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_address_customer_fullname'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='infororder',
            name='address',
        ),
        migrations.RemoveField(
            model_name='infororder',
            name='phone',
        ),
        migrations.AddField(
            model_name='infororder',
            name='customer',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='user.customer'),
        ),
    ]