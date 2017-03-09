# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-03-07 13:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserMessage',
            fields=[
                ('object_id', models.CharField(default='', max_length=50, primary_key=True, serialize=False, verbose_name='\u4e3b\u952e')),
                ('name', models.CharField(default='', max_length=20, verbose_name='\u7528\u6237\u540d')),
                ('email', models.EmailField(max_length=254, verbose_name='\u90ae\u7bb1')),
                ('address', models.CharField(max_length=100, verbose_name='\u8054\u7cfb\u5730\u5740')),
                ('message', models.CharField(max_length=500, verbose_name='\u7559\u8a00\u4fe1\u606f')),
            ],
            options={
                'ordering': ['-object_id'],
                'db_table': 'user_message',
                'verbose_name': '\u7528\u6237\u7559\u8a00\u4fe1\u606f',
                'verbose_name_plural': '\u7528\u6237\u7559\u8a00\u4fe1\u606f',
            },
        ),
    ]