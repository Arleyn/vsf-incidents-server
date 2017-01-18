# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-01-13 19:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0017_metricflag'),
    ]

    operations = [
        migrations.AddField(
            model_name='metricflag',
            name='manual_flag',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='metricflag',
            name='flag',
            field=models.NullBooleanField(default=False),
        ),
    ]