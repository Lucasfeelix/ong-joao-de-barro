from datetime import datetime
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist
from .models import Expenses


class ExpensestMixin(object):
    def get_queryset(self):
        super(ExpensestMixin, self).get_queryset()
        c = Expenses.objects.all().order_by('-created_at')
        if self.request.GET.get('service_type') == 'Aluguel':
            c = c.filter(service_type='Aluguel')
        elif self.request.GET.get('service_type') == 'Compra':
            c = c.filter(service_type='Compra')
        elif self.request.GET.get('service_type') == 'Devolução':
            c = c.filter(service_type='Devolução')
        elif self.request.GET.get('service_type') == 'Extorno':
            c = c.filter(service_type='Extorno')
        elif self.request.GET.get('service_type') == 'Pagamento':
            c = c.filter(service_type='Pagamento')
        return c
