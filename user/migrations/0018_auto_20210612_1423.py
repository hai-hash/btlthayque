# Generated by Django 3.1.7 on 2021-06-12 07:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0017_infororder_receive_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='shipment',
            name='name',
        ),
        migrations.AlterField(
            model_name='infororder',
            name='payment',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='user.payment'),
        ),
    ]
