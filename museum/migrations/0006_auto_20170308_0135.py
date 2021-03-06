# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-07 22:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('museum', '0005_author_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='painting',
            name='full_image',
            field=models.ImageField(null=True, upload_to='paintings', verbose_name='Полное изображение'),
        ),
        migrations.AlterField(
            model_name='painting',
            name='image',
            field=models.ImageField(upload_to='paintings', verbose_name='Изображение (~228x228)'),
        ),
    ]
