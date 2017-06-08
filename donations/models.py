from django.db import models
from core.models import TimeModel
from django.core.urlresolvers import reverse


C_TYPE = ((u'Aluguel', u'Aluguel'),
          (u'Compra', u'Compra'),
          (u'Devolução', u'Devolução'),
          (u'Doação', u'Doação'),
          (u'Extorno', u'Extorno'),
          (u'Recebimento', u'Recebimento'),
          (u'Pagamento', u'Pagamento'))


class Donors(TimeModel):
    name = models.CharField('Nome', max_length=100)
    slug = models.SlugField('Identificador', max_length=100)

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
                                    choices=C_TYPE, default='Recebimento')
    slug = models.SlugField('Identificador', max_length=100)
    donor = models.ForeignKey(Donors, verbose_name='Doador')
    item = models.CharField('Item', max_length=100)
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


class Expenses(TimeModel):
    service_type = models.CharField('Tipo de serviço', max_length=12,
                                    choices=C_TYPE, default='Compra')
    slug = models.SlugField('Identificador', max_length=100)
    item = models.CharField('Item', max_length=100)
    description = models.TextField('Descrição', blank=True)
    quantity = models.IntegerField('Quantidade')
    price = models.DecimalField('Preço', max_digits=6, decimal_places=2)
    date = models.DateTimeField('Data', auto_now_add=True)

    @property
    def total(self):
        return self.quantity * self.price

    def __str__(self):
        return str(self.service_type)

    class Meta:
        ordering = ['service_type']
        verbose_name = 'Despesa'
        verbose_name_plural = 'Despesas'

    # def get_absolute_url(self):
    #     return reverse('donations:donation_detail', kwargs={'pk': self.pk})


class ItemsExpenses(models.Model):
    expense_id = models.ForeignKey(Expenses, verbose_name='Nome',
                                   on_delete=models.CASCADE)
    name = models.CharField(verbose_name='Nome', max_length=100)
    description = models.TextField('Descrição', blank=True)
    quantity = models.IntegerField('Quantidade')
    price = models.DecimalField('Preço', max_digits=6, decimal_places=2)

    @property
    def total(self):
        return self.quantity * self.price

    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Itens'
