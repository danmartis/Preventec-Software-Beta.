# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-09-20 19:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modulos', '0002_auto_20170913_1859'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carpeta',
            name='fecha_inicio',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='carpeta',
            name='fecha_termino',
            field=models.DateField(blank=True, null=True),
        ),
    ]