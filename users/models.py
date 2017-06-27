# coding=utf-8
from django.db import models
from django.core.urlresolvers import reverse
from core.models import Address, PersonalInformations
from core.models import TimeStampedModel
from core.helpers.multiple_choices import SCHOLARITY, TIME


class Donors(Address, TimeStampedModel):
    name = models.CharField('Nome', max_length=100, unique=True)
    is_active = models.BooleanField('Ativo', help_text='Status do doador',
                                    default=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ['name']
        verbose_name = 'Doador'
        verbose_name_plural = 'Doadores'

    def get_absolute_url(self):
        return reverse('users:donors_detail', kwargs={'pk': self.pk})


class Students(Address, PersonalInformations, TimeStampedModel):
    scholarity = models.CharField('Escolaridade', choices=SCHOLARITY,
                                  max_length=100)
    school = models.CharField('Escola', blank=True, max_length=100)
    time = models.CharField('Período', choices=TIME, max_length=100)
    is_active = models.BooleanField('Ativo', help_text='Status do aluno',
                                    default=True)

    def __str__(self):
        return str(self.name + self.last_name)

    class Meta:
        ordering = ['name']
        verbose_name = 'Aluno'
        verbose_name_plural = 'Alunos'

    def get_absolute_url(self):
        return reverse('users:students_detail', kwargs={'pk': self.pk})
