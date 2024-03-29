# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-04 12:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0023_auto_20180304_2048'),
    ]

    operations = [
        migrations.CreateModel(
            name='AutomaticNews2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=100)),
                ('writer', models.CharField(max_length=50)),
                ('datetime', models.DateTimeField()),
                ('content', models.TextField()),
                ('image_raw', models.ImageField(upload_to='AutomaticNews/%Y/%m/%d')),
                ('image_predict', models.ImageField(upload_to='AutomaticNews/%Y/%m/%d')),
                ('report_pdf', models.FileField(upload_to='AutomaticNews/%Y/%m/%d')),
                ('submenu_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='web.SubMenu')),
            ],
        ),
    ]
