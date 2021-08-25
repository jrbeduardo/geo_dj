# Generated by Django 3.2.6 on 2021-08-24 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ip_address', '0003_measurement'),
    ]

    operations = [
        migrations.AddField(
            model_name='visitor',
            name='latitud',
            field=models.DecimalField(decimal_places=7, default=19.42847, max_digits=11),
        ),
        migrations.AddField(
            model_name='visitor',
            name='longitud',
            field=models.DecimalField(decimal_places=7, default=-99.12766, max_digits=11),
        ),
    ]
