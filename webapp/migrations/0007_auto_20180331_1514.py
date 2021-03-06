# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-03-31 09:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0006_auto_20180331_1450'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('searchedMovieName', models.CharField(max_length=40)),
                ('searchedMovieName2', models.CharField(max_length=40)),
                ('searchedMovieName3', models.CharField(max_length=40)),
            ],
        ),
        migrations.DeleteModel(
            name='Auth',
        ),
        migrations.DeleteModel(
            name='MovieData',
        ),
        migrations.DeleteModel(
            name='RecommendData',
        ),
    ]
