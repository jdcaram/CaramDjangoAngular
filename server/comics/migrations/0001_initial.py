# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-05 01:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ComicUniverse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=200)),
                ('universe_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Hero',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('secret_identity', models.CharField(max_length=200)),
                ('comic_universe', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='comics.ComicUniverse')),
            ],
        ),
    ]
