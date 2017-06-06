# coding=utf-8
from django import forms
from donations.models import Donations, Donors, Expenses, Items, Products


class DonationsAddForm(forms.ModelForm):
    class Meta:
        model = Donations
        fields = ['name', 'service_type', 'donor', 'quantity']
        readonly_fields = ('date')
