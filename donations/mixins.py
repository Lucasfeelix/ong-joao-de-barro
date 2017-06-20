from datetime import datetime
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist
from .models import Donations


class DonationstMixin(object):
    def get_queryset(self):
        super(DonationstMixin, self).get_queryset()
        c = Donations.objects.all().order_by('-created_at')
        if self.request.GET.get('service_type') == 'Doação':
            c = c.filter(service_type='Doação')
        elif self.request.GET.get('service_type') == 'Recebimento':
            c = c.filter(service_type='Recebimento')
        return c
