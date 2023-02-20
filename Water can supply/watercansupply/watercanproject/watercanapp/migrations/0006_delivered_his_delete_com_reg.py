# Generated by Django 4.1.7 on 2023-02-20 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watercanapp', '0005_usr_can_odr'),
    ]

    operations = [
        migrations.CreateModel(
            name='Delivered_his',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('phone_number', models.CharField(max_length=13)),
                ('address', models.CharField(max_length=150)),
                ('quantity', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='com_reg',
        ),
    ]
