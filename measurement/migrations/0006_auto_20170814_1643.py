# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-08-14 16:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0004_auto_20170814_1643'),
        ('measurement', '0005_auto_20170712_1550'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='DNS',
            new_name='DNSServer',
        ),
        migrations.AddField(
            model_name='flag',
            name='isp',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='event.ISP'),
        ),
        migrations.AlterField(
            model_name='probe',
            name='region',
            field=models.ForeignKey(blank=True, default=3718, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='probes', to='event.State'),
        ),
    ]