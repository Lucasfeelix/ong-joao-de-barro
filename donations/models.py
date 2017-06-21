from django.db import models
from core.models import TimeStampedModel
from django.core.urlresolvers import reverse
from core.helpers.multiple_choices import DONATIONS_TYPE
from users.models import Donors


class Donations(TimeStampedModel):
    service_type = models.CharField('Tipo de serviço', max_length=12,
                                    choices=DONATIONS_TYPE,
                                    default='Recebimento')
    donor = models.ForeignKey(Donors, verbose_name='Doador')
    item = models.CharField('Item', max_length=100, default='')
    description = models.TextField('Descrição', blank=True)
    quantity = models.PositiveSmallIntegerField('Quantidade', default=0)

    def __str__(self):
        return str(self.service_type)

    class Meta:
        ordering = ['service_type']
        verbose_name = 'Doação'
        verbose_name_plural = 'Doações'

    def get_absolute_url(self):
        return reverse('donations:donation_detail', kwargs={'pk': self.pk})
