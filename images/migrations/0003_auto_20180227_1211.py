# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-02-27 09:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0002_auto_20180226_2100'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='gallery',
            options={'ordering': ['-image']},
        ),
        migrations.AddField(
            model_name='gallery',
            name='url',
            field=models.URLField(default=1),
        ),
    ]
