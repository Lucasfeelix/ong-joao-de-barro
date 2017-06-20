from django.db import models
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from expenses.models import Expenses
from expenses.forms import ExpensesAddForm


class ExpensesListView(LoginRequiredMixin, ListView):
    template_name = 'expenses/expenses_list.html'
    context_object_name = 'expenses'
    paginate_by = 10
    # queryset = Expenses.objects.all().order_by('-date')

    def get_queryset(self):
        queryset = Expenses.objects.all().order_by('-created_at')
        q = self.request.GET.get('q', '')
        if q:
            queryset = queryset.filter(
                models.Q(item__icontains=q) |
                models.Q(description__icontains=q)
                # models.Q(donors__name__icontains=q)  # used like foreign key
            )
        elif self.request.GET.get('service_type') == 'Aluguel':
            queryset = queryset.filter(service_type='Aluguel')
        elif self.request.GET.get('service_type') == 'Compra':
            queryset = queryset.filter(service_type='Compra')
        elif self.request.GET.get('service_type') == 'Pagamento':
            queryset = queryset.filter(service_type='Pagamento')
        return queryset


class ExpensesDetailView(LoginRequiredMixin, DetailView):
    model = Expenses
    context_object_name = 'expenses'


class ExpensesCreateView(LoginRequiredMixin, CreateView):
    model = Expenses
    form_class = ExpensesAddForm


expenses = ExpensesListView.as_view()
expenses_detail = ExpensesDetailView.as_view()
expenses_add = ExpensesCreateView.as_view()
