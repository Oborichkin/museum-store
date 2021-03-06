# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-06 21:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('museum', '0003_auto_20170307_0013'),
    ]

    operations = [
        migrations.CreateModel(
            name='Painting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, verbose_name='Название')),
                ('slug', models.SlugField(max_length=15, verbose_name='URL')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание картины')),
                ('year', models.IntegerField(null=True, verbose_name='Год')),
                ('image', models.ImageField(upload_to='paintings', verbose_name='Изображение')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='museum.Author', verbose_name='Автор')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='museum.Category', verbose_name='Категория')),
                ('style', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='museum.Style', verbose_name='Направление')),
            ],
            options={
                'verbose_name': 'Картина',
                'verbose_name_plural': 'Картины',
            },
        ),
    ]
