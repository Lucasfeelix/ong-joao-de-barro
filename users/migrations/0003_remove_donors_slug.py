# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-21 04:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20170621_0130'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='donors',
            name='slug',
        ),
    ]
