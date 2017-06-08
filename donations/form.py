# coding=utf-8
from django import forms
from donations.models import Donations, Donors, Expenses, ItemsExpenses, C_TYPE


class DonationsAddForm(forms.ModelForm):
    class Meta:
        model = Donations
        fields = ['service_type', 'slug', 'donor', 'item', 'description',
                  'quantity']
        readonly_fields = ('date')


class ItemsForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        if not kwargs.get('initial'):
            kwargs['initial'] = {}

        if kwargs.get('instance'):
            kwargs['initial'].update({'total': kwargs.get('instance').total})

        super(ItemsForm, self).__init__(*args, **kwargs)

    total = forms.FloatField(widget=forms.NumberInput(
            attrs={'readonly': 'readonly'}), required=False)

    class Meta:
        model = ItemsExpenses
        exclude = []
