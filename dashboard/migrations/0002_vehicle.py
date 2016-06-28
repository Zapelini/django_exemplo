# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-28 21:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, verbose_name='nome')),
                ('model', models.CharField(max_length=100, verbose_name='model')),
                ('year', models.CharField(max_length=4, verbose_name='model')),
            ],
        ),
    ]
