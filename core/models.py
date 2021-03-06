# coding=utf-8
from django.db import models
from core.helpers.multiple_choices import UF


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    modified_at = models.DateTimeField('Modificado em', auto_now=True)

    class Meta:
        abstract = True


class Address(models.Model):
    address = models.CharField('Endereço', max_length=100, blank=True)
    number = models.IntegerField('Número')
    complement = models.CharField('Complemento', max_length=100, blank=True)
    neighborhood = models.CharField('Bairro', max_length=100, blank=True)
    city = models.CharField('Cidade', max_length=100, blank=True)
    state = models.CharField('Estado', max_length=16, choices=UF, blank=True)
    cep = models.CharField('CEP', max_length=8, blank=True)

    class Meta:
            abstract = True
