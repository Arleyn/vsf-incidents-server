# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-01-24 19:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0022_metricflag_ip'),
    ]

    operations = [
        migrations.AddField(
            model_name='metricflag',
            name='isp',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='metricflag',
            name='region',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='metricflag',
            name='target',
            field=models.CharField(default='', max_length=25),
            preserve_default=False,
        ),
    ]