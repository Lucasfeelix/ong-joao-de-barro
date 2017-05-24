from django.db import models
from core.models import TimeModel

C_TYPE = ((u'A', u'Aluguel'),
          (u'C', u'Compra'),
          (u'D', u'Devolução'),
          (u'O', u'Doação'),
          (u'E', u'Extorno'),
          (u'R', u'Recebimento'),
          (u'T', u'Troca'))


class Donors(TimeModel, models.Model):
    """
    ID | Name      |
    01 | João      |
    02 | Carrossel |
    """
    name = models.CharField('Nome', max_length=100)
    slug = models.SlugField('Identificador', max_length=100)

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ['name']
        verbose_name = 'Doador'
        verbose_name_plural = 'Doadores'

    def get_absolute_url(self):
        return reverse('donations:index', kwargs={'slug': self.slug})


class Products(TimeModel, models.Model):
    """
    ID | Name            | Description |
    01 | Camiseta        | Tamanho P   |
    02 | Pacote Sulfite  | Para ONG    |
    """
    name = models.CharField('Nome', max_length=100)
    slug = models.SlugField('Identificador', max_length=100)
    description = models.TextField('Descrição', blank=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ['name']
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'

    def get_absolute_url(self):
        return reverse('donations:index', kwargs={'slug': self.slug})


class Donations(TimeModel, models.Model):
    """
    ID | Name     | Item_type   | Donor     | Date  | Quantity |
    01 | Camiseta | Recebimento | Carrossel | 1/2/3 | 10       |
    02 | Agasalho | Doação      | ONG JDB   | 1/2/3 | 20       |
    """
    name = models.ForeignKey(Products, verbose_name='Nome')
    slug = models.SlugField('Identificador', max_length=100)
    service_type = models.CharField(max_length=12, choices=C_TYPE,
                                    default='Recebimento')
    donor = models.ForeignKey(Donors, verbose_name='Doador')
    date = models.DateTimeField('Data', auto_now_add=True)
    quantity = models.PositiveSmallIntegerField('Quantidade', default=0)

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ['name']
        verbose_name = 'Doação'
        verbose_name_plural = 'Doações'

    def get_absolute_url(self):
        return reverse('donations:index', kwargs={'slug': self.slug})


class Expenses(TimeModel, models.Model):
    """
    ID | Name   | Type   | Description    | Date  | Quantity | Price | Total
    01 | Tshirt | Compra | Tshirts to ONG | 1/2/3 | 20       | 30    | 600
    """
    name = models.ForeignKey(Products, verbose_name='Serviço')
    slug = models.SlugField('Identificador', max_length=100)
    service_type = models.CharField(max_length=12, choices=C_TYPE)
    description = models.TextField('Descrição', blank=True)
    date = models.DateTimeField('Data', auto_now_add=True)
    quantity = models.IntegerField('Quantidade')
    price = models.DecimalField('Preço', max_digits=6, decimal_places=2)

    @property
    def total(self):
        return self.quantity * self.price

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ['name']
        verbose_name = 'Despesa'
        verbose_name_plural = 'Despesas'

    def get_absolute_url(self):
        return reverse('donations:index', kwargs={'slug': self.slug})
