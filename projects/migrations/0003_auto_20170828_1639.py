# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-08-28 21:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20170828_1631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='fecha_termino',
            field=models.DateField(blank=True, null=True),
        ),
    ]
