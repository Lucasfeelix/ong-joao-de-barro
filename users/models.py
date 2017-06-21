# coding=utf-8
from django.db import models
from django.core.urlresolvers import reverse
from core.models import Address, TimeStampedModel


class Donors(TimeStampedModel, Address):
    name = models.CharField('Nome', max_length=100, unique=True)
    # slug = models.SlugField('Identificador', max_length=100, default='')
    is_active = models.BooleanField('Ativo', default=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ['name']
        verbose_name = 'Doador'
        verbose_name_plural = 'Doadores'

    def get_absolute_url(self):
        return reverse('users:donors_detail', kwargs={'pk': self.pk})
