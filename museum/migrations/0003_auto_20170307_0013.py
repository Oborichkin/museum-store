# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-06 21:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('museum', '0002_auto_20170304_0258'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='painting',
            name='author',
        ),
        migrations.RemoveField(
            model_name='painting',
            name='category',
        ),
        migrations.RemoveField(
            model_name='painting',
            name='style',
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterField(
            model_name='author',
            name='name',
            field=models.CharField(max_length=60, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='author',
            name='slug',
            field=models.SlugField(max_length=60, verbose_name='URL Автора'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=30, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(max_length=15, verbose_name='URL Категории'),
        ),
        migrations.AlterField(
            model_name='molding',
            name='image',
            field=models.ImageField(upload_to='molding', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='molding',
            name='name',
            field=models.CharField(max_length=30, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='molding',
            name='price',
            field=models.FloatField(verbose_name='Цена (за метр)'),
        ),
        migrations.AlterField(
            model_name='molding',
            name='slug',
            field=models.SlugField(max_length=15, verbose_name='Имя CSS класса'),
        ),
        migrations.AlterField(
            model_name='molding',
            name='width',
            field=models.IntegerField(verbose_name='Ширина (мм)'),
        ),
        migrations.AlterField(
            model_name='service',
            name='name',
            field=models.CharField(max_length=60, verbose_name='Название услуги'),
        ),
        migrations.AlterField(
            model_name='service',
            name='price',
            field=models.FloatField(verbose_name='Цена (за кв. м)'),
        ),
        migrations.AlterField(
            model_name='style',
            name='name',
            field=models.CharField(max_length=30, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='style',
            name='slug',
            field=models.SlugField(max_length=15, verbose_name='URL Направления'),
        ),
        migrations.DeleteModel(
            name='Painting',
        ),
    ]