# Generated by Django 3.0.6 on 2020-05-27 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TravelBook', '0008_auto_20200527_1802'),
    ]

    operations = [
        migrations.AlterField(
            model_name='destination',
            name='start',
            field=models.DateField(blank=True, null=True),
        ),
    ]
