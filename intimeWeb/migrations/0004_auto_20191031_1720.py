# Generated by Django 2.2.6 on 2019-10-31 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('intimeWeb', '0003_auto_20191031_1651'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flight',
            name='date',
            field=models.DateTimeField(),
        ),
    ]
