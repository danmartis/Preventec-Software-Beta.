# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-09-28 18:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modulos', '0013_auto_20170928_1136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subcarpeta',
            name='default',
            field=models.BooleanField(default=True),
        ),
    ]
