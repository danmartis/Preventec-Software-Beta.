# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-10-30 22:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0018_auto_20171028_1323'),
        ('modulos', '0029_auto_20171022_1954'),
    ]

    operations = [
        migrations.AddField(
            model_name='documento',
            name='firmas',
            field=models.ManyToManyField(blank=True, null=True, to='profiles.Profile'),
        ),
    ]