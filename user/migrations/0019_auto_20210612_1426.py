# Generated by Django 3.1.7 on 2021-06-12 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0018_auto_20210612_1423'),
    ]

    operations = [
        migrations.AlterField(
            model_name='infororder',
            name='payment',
            field=models.CharField(default='Thanh toán khi nhận hàng', max_length=100),
        ),
    ]
