# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-03-15 14:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plugins', '0005_auto_20170315_1354'),
    ]

    operations = [
        migrations.AddField(
            model_name='http',
            name='body_proportion',
            field=models.FloatField(default=1.0),
            preserve_default=False,
        ),
    ]
