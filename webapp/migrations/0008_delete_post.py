# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-03-31 09:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0007_auto_20180331_1514'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Post',
        ),
    ]
