# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-25 08:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='publish',
            field=models.BooleanField(default=False),
        ),
    ]
