from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView, UpdateView
from django.views.generic import DetailView
from django.core.urlresolvers import reverse_lazy
from donations.models import Donations
from donations.forms import DonationsAddForm


class IndexView(TemplateView):
    template_name = 'donations/index.html'


class DonationsListView(ListView):
    template_name = 'donations/donations_list.html'
    context_object_name = 'donations'
    model = Donations
    queryset = Donations.objects.all().order_by('-date')
    paginate_by = 10


class DonationsCreateView(CreateView):
    model = Donations
    form_class = DonationsAddForm


class DonationsUpdateView(UpdateView):
    model = Donations
    template_name = 'donations/donations_update.html'
    fields = ['name', 'service_type', 'donor', 'quantity']
    success_url = reverse_lazy('donations:donation')

    def get_object(self):
        return self.object.all()


index = IndexView.as_view()
donations = DonationsListView.as_view()
donations_add = DonationsCreateView.as_view()
donations_update = DonationsUpdateView.as_view()
donations_detail = DetailView.as_view(model=Donations,
                                      context_object_name='donations')
