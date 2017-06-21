# coding=utf-8
from django.shortcuts import render
from django.views.generic import CreateView, TemplateView, UpdateView, FormView
from django.views.generic import DetailView, ListView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from users.models import Donors
from users.forms import DonorsAddForm


class DonorsListView(LoginRequiredMixin, ListView):
    template_name = 'users/donors_list.html'
    model = Donors
    context_object_name = 'donors'
    paginate_by = 10
    queryset = Donors.objects.all().order_by('-created_at')


class DonorsCreateView(LoginRequiredMixin, CreateView):
    model = Donors
    form_class = DonorsAddForm


class DonorsDetailView(LoginRequiredMixin, DetailView):
    model = Donors
    context_object_name = 'donors'


donors = DonorsListView.as_view()
donors_add = DonorsCreateView.as_view()
donors_detail = DonorsDetailView.as_view()
