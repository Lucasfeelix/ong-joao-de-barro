# coding=utf-8
from django import forms
from .models import Donors, Students, Employees


class DonorsAddForm(forms.ModelForm):
    class Meta:
        model = Donors
        fields = ['is_active', 'name', 'email', 'phone', 'cellphone',
                  'address', 'number', 'complement', 'neighborhood',
                  'city', 'state', 'cep', 'comments']
        readonly_fields = ('created_at')


class StudentsAddForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = ['is_active', 'name', 'last_name', 'date_of_birth', 'gender',
                  'mothers_name', 'fathers_name', 'rg', 'cpf', 'scholarity',
                  'school', 'time', 'occupation', 'civil_status',  'address',
                  'number', 'complement', 'neighborhood', 'city', 'state',
                  'cep', 'email', 'phone', 'cellphone', 'comments']
        readonly_fields = ('created_at')


class EmployeesAddForm(forms.ModelForm):
    class Meta:
        model = Employees
        fields = ['is_active', 'name', 'last_name', 'date_of_birth', 'gender',
                  'mothers_name', 'fathers_name', 'rg', 'cpf', 'occupation',
                  'bag_helped', 'value', 'employees_type', 'civil_status',
                  'address', 'number', 'complement', 'neighborhood', 'city',
                  'state', 'cep', 'email', 'phone', 'cellphone', 'comments']
        readonly_fields = ('created_at')
