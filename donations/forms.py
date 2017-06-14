# coding=utf-8
from django import forms
from donations.models import Donations, Donors


class DonationsAddForm(forms.ModelForm):
    class Meta:
        model = Donations
        fields = ['service_type', 'donor', 'item', 'description',
                  'quantity']
        readonly_fields = ('date')

#
# class ExpensesForm(forms.ModelForm):
#     def __init__(self, *args, **kwargs):
#         if not kwargs.get('initial'):
#             kwargs['initial'] = {}
#
#         if kwargs.get('instance'):
#             kwargs['initial'].update({'total': kwargs.get('instance').total})
#
#         super(ExpensesForm, self).__init__(*args, **kwargs)
#
#     total = forms.FloatField(widget=forms.NumberInput(
#             attrs={'readonly': 'readonly'}), required=False)
#
#     class Meta:
#         model = Expenses
#         exclude = []
