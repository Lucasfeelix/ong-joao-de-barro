from django.db import models
from core.models import TimeModel
from django.core.urlresolvers import reverse
from core.helpers.multiple_choices import DONATIONS_TYPE


class Donors(TimeModel):
    name = models.CharField('Nome', max_length=100)
    slug = models.SlugField('Identificador', max_length=100, default='')

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ['name']
        verbose_name = 'Doador'
        verbose_name_plural = 'Doadores'

    def get_absolute_url(self):
        return reverse('donations:donation_detail', kwargs={'slug': self.slug})


class Donations(TimeModel):
    service_type = models.CharField('Tipo de serviço', max_length=12,
                                    choices=DONATIONS_TYPE,
                                    default='Recebimento')
    donor = models.ForeignKey(Donors, verbose_name='Doador')
    item = models.CharField('Item', max_length=100, default='')
    description = models.TextField('Descrição', blank=True)
    quantity = models.PositiveSmallIntegerField('Quantidade', default=0)
    date = models.DateTimeField('Data', auto_now_add=True)

    def __str__(self):
        return str(self.service_type)

    class Meta:
        ordering = ['service_type']
        verbose_name = 'Doação'
        verbose_name_plural = 'Doações'

    def get_absolute_url(self):
        return reverse('donations:donation_detail', kwargs={'pk': self.pk})
