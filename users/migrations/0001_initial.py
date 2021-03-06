# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-21 04:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Donors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Modificado em')),
                ('address', models.CharField(blank=True, max_length=100, verbose_name='Endereço')),
                ('number', models.IntegerField(verbose_name='Número')),
                ('complement', models.CharField(blank=True, max_length=100, verbose_name='Complemento')),
                ('neighborhood', models.CharField(blank=True, max_length=100, verbose_name='Bairro')),
                ('city', models.CharField(blank=True, max_length=100, verbose_name='Cidade')),
                ('state', models.CharField(blank=True, choices=[('Acre', 'Acre'), ('Alagoas', 'Alagoas'), ('Amazonas', 'Amazonas'), ('Amapá', 'Amapá'), ('Bahia', 'Bahia'), ('Ceará', 'Ceará'), ('Brasília', 'Brasília'), ('Espírito Santo', 'Espírito Santo'), ('Goiás', 'Goiás'), ('Maranhão', 'Maranhão'), ('Minas Gerais', 'Minas Gerais'), ('Mato Grosso do Sul', 'Mato Grosso do Sul'), ('Mato Grosso', 'Mato Grosso'), ('Pará', 'Pará'), ('Paraíba', 'Paraíba'), ('Pernambuco', 'Pernambuco'), ('Piauí', 'Piauí'), ('Paraná', 'Paraná'), ('Rio de Janeiro', 'Rio de Janeiro'), ('Rio Grande do Norte', 'Rio Grande do Norte'), ('Rondônia', 'Rondônia'), ('Roraima', 'Roraima'), ('Rio Grande do Sul', 'Rio Grande do Sul'), ('Santa Catarina', 'Santa Catarina'), ('Sergipe', 'Sergipe'), ('São Paulo', 'São Paulo'), ('Tocantins', 'Tocantins')], max_length=16, verbose_name='Estado')),
                ('cep', models.CharField(blank=True, max_length=8, verbose_name='CEP')),
                ('name', models.CharField(blank=True, max_length=100, verbose_name='Nome')),
                ('slug', models.SlugField(default='', max_length=100, verbose_name='Identificador')),
                ('is_active', models.BooleanField(default=True, verbose_name='Ativo')),
            ],
            options={
                'verbose_name': 'Doador',
                'verbose_name_plural': 'Doadores',
                'ordering': ['name'],
            },
        ),
    ]
