# Generated by Django 2.2 on 2020-01-24 06:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BLOGAPP', '0004_auto_20200111_1121'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog_table1',
            name='Date',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 24, 12, 20, 53, 796074), null=True),
        ),
    ]
