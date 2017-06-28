# coding=utf-8
from django.db import models
from django.core.urlresolvers import reverse
from core.models import Address, PersonalInformations
from core.models import TimeStampedModel
from core.helpers.multiple_choices import SCHOLARITY, TIME, EMPLOYEES_TYPE


class Donors(Address, TimeStampedModel):
    name = models.CharField('Nome', max_length=100, unique=True)
    is_active = models.BooleanField('Ativo', help_text='Status do doador',
                                    default=True)
    email = models.EmailField('E-mail', unique=True, default='')
    phone = models.CharField('Telefone ', max_length=10, blank=True)
    cellphone = models.CharField('Celular', max_length=11, blank=True)
    comments = models.TextField('Observações', blank=True)

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


class Employees(Address, PersonalInformations, TimeStampedModel):
    bag_helped = models.BooleanField('Bolsa auxílio', default=False,
                                     help_text='O funcionário será remunerado\
                                     pelas atividades prestadas a ONG?')
    value = models.DecimalField('Valor', max_digits=6, decimal_places=2,
                                default=0)
    employees_type = models.CharField('Tipo de serviço', max_length=100,
                                      choices=EMPLOYEES_TYPE)
    is_active = models.BooleanField('Ativo', help_text='Status do aluno',
                                    default=True)

    def __str__(self):
        return str(self.name + self.last_name)

    class Meta:
        ordering = ['name']
        verbose_name = 'Funcionário'
        verbose_name_plural = 'Funcionários'

    def get_absolute_url(self):
        return reverse('users:employees_detail', kwargs={'pk': self.pk})
