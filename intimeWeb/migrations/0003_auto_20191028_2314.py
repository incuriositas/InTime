# Generated by Django 2.2.6 on 2019-10-28 14:14

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('intimeWeb', '0002_auto_20191028_2306'),
    ]

    operations = [
        migrations.AddField(
            model_name='flight',
            name='predictTime',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='flight',
            name='schTime',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 28, 14, 14, 34, 331471, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='flight',
            name='airFln',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='flight',
            name='airline',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='flight',
            name='airport',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='flight',
            name='arrived',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='flight',
            name='boarding',
            field=models.CharField(max_length=50),
        ),
    ]
