# Generated by Django 3.2.9 on 2022-02-12 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stronaK', '0004_auto_20211124_1358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='oldknight',
            name='date_birth',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='oldknight',
            name='date_death',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='song',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
