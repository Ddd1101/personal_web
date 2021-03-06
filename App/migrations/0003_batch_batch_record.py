# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-16 02:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_auto_20171213_1147'),
    ]

    operations = [
        migrations.CreateModel(
            name='Batch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datasetName', models.CharField(max_length=50)),
                ('batchName', models.CharField(max_length=50)),
                ('recordDate', models.DateField()),
                ('recorder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.User')),
            ],
        ),
        migrations.CreateModel(
            name='Batch_record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial_no', models.IntegerField()),
                ('capacity', models.FloatField()),
                ('loss_angle_tangent', models.FloatField()),
                ('leakage_current', models.FloatField()),
                ('batch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.Batch')),
            ],
        ),
    ]
