# Generated by Django 3.0.6 on 2020-05-26 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TravelBook', '0005_auto_20200510_1719'),
    ]

    operations = [
        migrations.AddField(
            model_name='destination',
            name='start',
            field=models.DateField(blank=True, null=True),
        ),
    ]
