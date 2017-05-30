from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.core.urlresolvers import reverse_lazy
from donations.models import Donations


class IndexView(TemplateView):
    template_name = 'donations/index.html'


class DonationsListView(ListView):
    template_name = 'donations/donations_list.html'
    context_object_name = 'donations'
    model = Donations
    paginate_by = 10


index = IndexView.as_view()
donations = DonationsListView.as_view()
