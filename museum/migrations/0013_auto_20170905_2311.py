# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-05 20:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('museum', '0012_auto_20170824_1711'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='item',
            options={'verbose_name': 'Товар', 'verbose_name_plural': 'Товары'},
        ),
    ]