# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-04 09:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0013_auto_20180304_1827'),
    ]

    operations = [
        migrations.AlterField(
            model_name='automaticnews',
            name='datetime',
            field=models.DateTimeField(),
        ),
    ]
