from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView, UpdateView
from django.views.generic import DetailView
from django.core.urlresolvers import reverse_lazy
from donations.models import Donations
from donations.form import DonationsAddForm


class IndexView(TemplateView):
    template_name = 'donations/index.html'


class DonationsListView(ListView):
    template_name = 'donations/donations_list.html'
    context_object_name = 'donations'
    model = Donations
    paginate_by = 10


class DonationsCreateView(CreateView):
    model = Donations
    form_class = DonationsAddForm
    # success_url = reverse_lazy('donations:donation')
    # template_name = 'donations/donations_add.html'
    # context_object_name = 'donations'


class DonationsUpdateView(UpdateView):
    model = Donations
    template_name = 'donations/donations_update.html'
    fields = ['name', 'service_type', 'donor', 'quantity']
    success_url = reverse_lazy('donations:donation')

    def get_object(self):
        return self.object.all()


# def donation_detail(request, slug):
#     donation = Donations.objects.get(slug=slug)
#     context = {
#         'donations': donations
#     }
#     return render(request, 'donations/donations-detail.html', context)


index = IndexView.as_view()
donations = DonationsListView.as_view()
donations_add = DonationsCreateView.as_view()
donations_update = DonationsUpdateView.as_view()
donations_detail = DetailView.as_view(model=Donations, context_object_name = 'donations')
