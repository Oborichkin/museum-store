# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-01-30 18:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('museum', '0019_auto_20180130_2052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='index',
            field=models.CharField(max_length=32),
        ),
    ]
