from django.db import models
from django.core.urlresolvers import reverse
from core.models import TimeStampedModel
from core.helpers.multiple_choices import EXPENSES_TYPE, UNIT_TYPE


class Expenses(TimeStampedModel):
    service_type = models.CharField('Tipo de serviço', max_length=12,
                                    choices=EXPENSES_TYPE, default='Compra')
    item = models.CharField('Item', max_length=100, default='')
    description = models.TextField('Descrição', blank=True)
    quantity = models.IntegerField('Quantidade', default=0)
    unit = models.CharField('Unidade', max_length=14, choices=UNIT_TYPE,
                            default='')
    price = models.DecimalField('Preço', max_digits=6, decimal_places=2,
                                default=0)

    @property
    def total(self):
        return self.quantity * self.price

    def __str__(self):
        return str(self.service_type)

    class Meta:
        ordering = ['service_type']
        verbose_name = 'Despesa'
        verbose_name_plural = 'Despesas'

    def get_absolute_url(self):
        return reverse('expenses:expense_detail', kwargs={'pk': self.pk})
