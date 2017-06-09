# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-09 02:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donations', '0003_auto_20170607_1353'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='itemsdonations',
            name='donation_id',
        ),
        migrations.AddField(
            model_name='donations',
            name='description',
            field=models.TextField(blank=True, verbose_name='Descrição'),
        ),
        migrations.AddField(
            model_name='donations',
            name='item',
            field=models.CharField(default='', max_length=100, verbose_name='Item'),
        ),
        migrations.AddField(
            model_name='donors',
            name='slug',
            field=models.SlugField(default='', max_length=100, verbose_name='Identificador'),
        ),
        migrations.AddField(
            model_name='expenses',
            name='item',
            field=models.CharField(default='', max_length=100, verbose_name='Item'),
        ),
        migrations.AddField(
            model_name='expenses',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6, verbose_name='Preço'),
        ),
        migrations.AddField(
            model_name='expenses',
            name='quantity',
            field=models.IntegerField(default=0, verbose_name='Quantidade'),
        ),
        migrations.DeleteModel(
            name='ItemsDonations',
        ),
    ]
