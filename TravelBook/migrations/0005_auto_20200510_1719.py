# Generated by Django 3.0.6 on 2020-05-10 15:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TravelBook', '0004_auto_20200510_1703'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='destination',
            name='end',
        ),
        migrations.RemoveField(
            model_name='destination',
            name='start',
        ),
    ]
