# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-03-28 07:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0007_auto_20180326_1554'),
    ]

    operations = [
        migrations.AlterField(
            model_name='batch',
            name='forge_rate',
            field=models.FloatField(default=None),
        ),
        migrations.AlterField(
            model_name='batch',
            name='mistake_rate',
            field=models.FloatField(default=None),
        ),
    ]
