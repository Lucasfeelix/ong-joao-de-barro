# coding=utf-8
from django import forms
from .models import Donors


class DonorsAddForm(forms.ModelForm):
    class Meta:
        model = Donors
        fields = ['is_active', 'name', 'address', 'number',
                  'complement', 'neighborhood', 'city', 'state', 'cep']
        readonly_fields = ('created_at')
