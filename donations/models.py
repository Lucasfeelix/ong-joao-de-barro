from django.db import models
from core.models import TimeModel

C_TYPE = ((u'Aluguel', u'Aluguel'),
          (u'Compra', u'Compra'),
          (u'Devolução', u'Devolução'),
          (u'Doação', u'Doação'),
          (u'Extorno', u'Extorno'),
          (u'Recebimento', u'Recebimento'),
          (u'Pagamento', u'Pagamento'))


class Donors(TimeModel):
    """
    ID | Name      |
    01 | João      |
    02 | Carrossel |
    """
    name = models.CharField('Nome', max_length=100)

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ['name']
        verbose_name = 'Doador'
        verbose_name_plural = 'Doadores'


class Products(TimeModel):
    """
    ID | Name            | Description |
    01 | Camiseta        | Tamanho P   |
    02 | Pacote Sulfite  | Para ONG    |
    """
    name = models.CharField('Nome', max_length=100)
    description = models.TextField('Descrição', blank=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ['name']
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'


class Donations(TimeModel):
    """
    ID | Name     | Item_type   | Donor     | Date  | Quantity |
    01 | Camiseta | Recebimento | Carrossel | 1/2/3 | 10       |
    02 | Agasalho | Doação      | ONG JDB   | 1/2/3 | 20       |
    """
    name = models.ForeignKey(Products, verbose_name='Nome')
    service_type = models.CharField('Tipo de serviço', max_length=12,
                                    choices=C_TYPE, default='Recebimento')
    donor = models.ForeignKey(Donors, verbose_name='Doador')
    date = models.DateTimeField('Data', auto_now_add=True)
    quantity = models.PositiveSmallIntegerField('Quantidade', default=0)

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ['name']
        verbose_name = 'Doação'
        verbose_name_plural = 'Doações'


class Expenses(TimeModel):
    """
    ID | Name   | Type   | Description    | Date  |
    01 | Tshirt | Compra | Tshirts to ONG | 1/2/3 |
    """
    name = models.ForeignKey(Products, verbose_name='Serviço')
    service_type = models.CharField('Tipo de serviço', max_length=12,
                                    choices=C_TYPE, default='Compra')
    description = models.TextField('Descrição', blank=True)
    date = models.DateTimeField('Data', auto_now_add=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ['name']
        verbose_name = 'Despesa'
        verbose_name_plural = 'Despesas'


class Items(models.Model):
    """
    ID | Name   | Quantity | Price | Total
    01 | Tshirt | 20       | 30    | 600
    """
    expense_id = models.ForeignKey(Expenses, verbose_name='Nome',
                                   on_delete=models.CASCADE)
    name = models.CharField(verbose_name='Nome', max_length=100)
    quantity = models.IntegerField('Quantidade')
    price = models.DecimalField('Preço', max_digits=6, decimal_places=2)

    @property
    def total(self):
        return self.quantity * self.price

    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Itens'
