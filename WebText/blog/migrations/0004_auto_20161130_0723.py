# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-30 07:23
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_blogmod_created_on'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogmod',
            name='created_on',
        ),
        migrations.AddField(
            model_name='blogmod',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
