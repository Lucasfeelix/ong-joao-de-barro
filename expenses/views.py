from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from expenses.models import Expenses
from expenses.forms import ExpensesAddForm


class ExpensesListView(LoginRequiredMixin, ListView):
    template_name = 'expenses/expenses_list.html'
    context_object_name = 'expenses'
    model = Expenses
    queryset = Expenses.objects.all().order_by('-date')
    paginate_by = 10


class ExpensesDetailView(LoginRequiredMixin, DetailView):
    model = Expenses
    context_object_name = 'expenses'


class ExpensesCreateView(LoginRequiredMixin, CreateView):
    model = Expenses
    form_class = ExpensesAddForm


expenses = ExpensesListView.as_view()
expenses_detail = ExpensesDetailView.as_view()
expenses_add = ExpensesCreateView.as_view()
