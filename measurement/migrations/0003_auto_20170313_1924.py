# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-03-13 19:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0002_auto_20170313_1921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flag',
            name='flag',
            field=models.NullBooleanField(db_index=True, default=False),
        ),
        migrations.AlterField(
            model_name='flag',
            name='is_flag',
            field=models.BooleanField(db_index=True, default=False),
        ),
        migrations.AlterField(
            model_name='flag',
            name='manual_flag',
            field=models.BooleanField(db_index=True, default=False),
        ),
    ]