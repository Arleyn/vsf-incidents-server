# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-06 21:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0013_auto_20161206_2106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='probe',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='probes', to='measurement.Country'),
        ),
        migrations.AlterField(
            model_name='probe',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='probes', to='measurement.State'),
        ),
    ]
