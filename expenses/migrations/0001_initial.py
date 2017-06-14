# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-14 01:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Expenses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Modificado em')),
                ('service_type', models.CharField(choices=[('Aluguel', 'Aluguel'), ('Compra', 'Compra'), ('Devolução', 'Devolução'), ('Extorno', 'Extorno'), ('Pagamento', 'Pagamento')], default='Compra', max_length=12, verbose_name='Tipo de serviço')),
                ('item', models.CharField(default='', max_length=100, verbose_name='Item')),
                ('description', models.TextField(blank=True, verbose_name='Descrição')),
                ('quantity', models.IntegerField(default=0, verbose_name='Quantidade')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=6, verbose_name='Preço')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Data')),
            ],
            options={
                'verbose_name': 'Despesa',
                'verbose_name_plural': 'Despesas',
                'ordering': ['service_type'],
            },
        ),
    ]