# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-03-09 21:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='metric',
            name='report_filename',
            field=models.CharField(max_length=250),
        ),
    ]
