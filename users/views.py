# coding=utf-8
from django.db.models import Q
from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DetailView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from users.models import Donors
from users.forms import DonorsAddForm


class DonorsListView(LoginRequiredMixin, ListView):
    template_name = 'users/donors_list.html'
    model = Donors
    context_object_name = 'donors'
    paginate_by = 10
    queryset = Donors.objects.all().order_by('-created_at')

    def get_queryset(self):
        queryset = Donors.objects.all().order_by('-created_at')
        q = self.request.GET.get('q', '')
        if q:
            queryset = queryset.filter(Q(name__icontains=q))
        elif self.request.GET.get('is_active') == 'True':
            queryset = queryset.filter(is_active=1)
        elif self.request.GET.get('is_active') == 'False':
            queryset = queryset.filter(is_active=0)
        return queryset


class DonorsCreateView(LoginRequiredMixin, CreateView):
    model = Donors
    form_class = DonorsAddForm


class DonorsUpdateView(LoginRequiredMixin, UpdateView):
    model = Donors
    template_name_suffix = '_update_form'
    fields = ['is_active', 'name', 'address', 'number', 'complement',
              'neighborhood', 'city', 'state', 'cep']


class DonorsDetailView(LoginRequiredMixin, DetailView):
    model = Donors
    context_object_name = 'donors'


donors_list = DonorsListView.as_view()
donors_add = DonorsCreateView.as_view()
donors_update = DonorsUpdateView.as_view()
donors_detail = DonorsDetailView.as_view()
