# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-06 21:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0014_auto_20161206_2108'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='probe',
            name='country',
        ),
        migrations.RemoveField(
            model_name='probe',
            name='region',
        ),
    ]
