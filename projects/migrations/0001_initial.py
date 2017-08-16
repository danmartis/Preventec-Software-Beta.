# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-08-15 23:41
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import projects.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('tipo', models.CharField(max_length=20)),
                ('direccion', models.CharField(max_length=20)),
                ('slug', models.SlugField(unique=True)),
                ('image', models.ImageField(blank=True, height_field='height_field', null=True, upload_to=projects.models.upload_location, width_field='width_field')),
                ('height_field', models.IntegerField(default=0)),
                ('width_field', models.IntegerField(default=0)),
                ('draft', models.BooleanField(default=False)),
                ('fecha_inicio', models.DateField(auto_now=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('fecha_termino', models.DateTimeField(auto_now_add=True)),
                ('admindor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='admindor', to=settings.AUTH_USER_MODEL)),
                ('gerente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gerente', to=settings.AUTH_USER_MODEL)),
                ('supervisor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='supervisor', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
