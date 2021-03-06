# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-03-21 08:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0004_batch_sequence_prob'),
    ]

    operations = [
        migrations.RenameField(
            model_name='batch',
            old_name='batchName',
            new_name='batch_name',
        ),
        migrations.RenameField(
            model_name='batch',
            old_name='datasetName',
            new_name='dataset_name',
        ),
        migrations.RenameField(
            model_name='batch',
            old_name='sequence_prob',
            new_name='forge_rate',
        ),
        migrations.RenameField(
            model_name='batch',
            old_name='recordDate',
            new_name='record_data',
        ),
        migrations.AddField(
            model_name='batch',
            name='mistake_rate',
            field=models.FloatField(default=0.0),
        ),
    ]
