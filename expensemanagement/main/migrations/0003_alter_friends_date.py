# Generated by Django 5.0.6 on 2024-06-11 17:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_friends_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friends',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 11, 17, 31, 38, 299349), null=True),
        ),
    ]
