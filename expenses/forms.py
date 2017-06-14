# coding=utf-8
from django import forms
from expenses.models import Expenses


class ExpensesAddForm(forms.ModelForm):
    class Meta:
        model = Expenses
        fields = ['service_type', 'item', 'description', 'quantity', 'unit',
                  'price']
        readonly_fields = ('date')
