# coding=utf-8
from django.db import models
from core.helpers.multiple_choices import UF, CIVIL_STATUS, GENDER


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


class PersonalInformations(models.Model):
    name = models.CharField('Nome', max_length=50)
    last_name = models.CharField('Sobrenome', max_length=50)
    email = models.EmailField('E-mail', unique=True)
    date_of_birth = models.DateField('Data de nascimento', auto_now=False)
    gender = models.CharField('Gênero', choices=GENDER, max_length=14)
    civil_status = models.CharField('Estado civil', choices=CIVIL_STATUS,
                                    max_length=14)
    mothers_name = models.CharField('Mãe', max_length=100)
    fathers_name = models.CharField('Pai', blank=True, max_length=100)
    occupation = models.CharField('Profissão', max_length=70)
    rg = models.CharField('RG', unique=True, max_length=9)
    cpf = models.CharField('CPF', unique=True, max_length=11)
    phone = models.CharField('Telefone ', max_length=20, blank=True)
    cellphone = models.CharField('Celular', max_length=20, blank=True)
    comments = models.TextField('Observações', blank=True)

    class Meta:
        abstract = True
