# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-12-18 19:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DriverApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='requests',
            name='completed_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='requests',
            name='picked_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]