# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-05-26 02:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leaderboard', '0005_auto_20180526_0250'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='winning_score',
            field=models.IntegerField(default=None),
        ),
    ]
