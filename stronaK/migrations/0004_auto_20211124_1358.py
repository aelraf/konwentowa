# Generated by Django 3.2.7 on 2021-11-24 12:58

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('stronaK', '0003_auto_20211120_1755'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'ordering': ['-date']},
        ),
        migrations.AlterField(
            model_name='news',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 11, 24, 12, 58, 13, 587115, tzinfo=utc)),
        ),
    ]
