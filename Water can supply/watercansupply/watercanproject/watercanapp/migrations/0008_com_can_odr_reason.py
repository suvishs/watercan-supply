# Generated by Django 4.1.7 on 2023-02-20 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watercanapp', '0007_com_can_odr'),
    ]

    operations = [
        migrations.AddField(
            model_name='com_can_odr',
            name='reason',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
