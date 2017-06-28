# coding=utf-8
from django.db.models import Q
from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DetailView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from users.models import Donors, Students, Employees
from users.forms import DonorsAddForm, StudentsAddForm, EmployeesAddForm


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
    fields = ['is_active', 'name', 'email', 'phone', 'cellphone', 'address',
              'number', 'complement', 'neighborhood', 'city', 'state', 'cep',
              'comments']


class DonorsDetailView(LoginRequiredMixin, DetailView):
    model = Donors
    context_object_name = 'donors'


class StudentsListView(LoginRequiredMixin, ListView):
    template_name = 'users/students_list.html'
    model = Students
    context_object_name = 'students'
    paginate_by = 10
    queryset = Students.objects.all().order_by('-created_at')

    def get_queryset(self):
        queryset = Students.objects.all().order_by('-created_at')
        q = self.request.GET.get('q', '')
        if q:
            queryset = queryset.filter(Q(name__icontains=q))
        elif self.request.GET.get('is_active') == 'True':
            queryset = queryset.filter(is_active=1)
        elif self.request.GET.get('is_active') == 'False':
            queryset = queryset.filter(is_active=0)
        return queryset


class StudentsCreateView(LoginRequiredMixin, CreateView):
    model = Students
    form_class = StudentsAddForm


class StudentsUpdateView(LoginRequiredMixin, UpdateView):
    model = Students
    template_name_suffix = '_update_form'
    fields = ['is_active', 'name', 'last_name', 'date_of_birth', 'gender',
              'mothers_name', 'fathers_name', 'rg', 'cpf', 'scholarity',
              'school', 'time', 'occupation', 'civil_status',  'address',
              'number', 'complement', 'neighborhood', 'city', 'state',
              'cep', 'email', 'phone', 'cellphone', 'comments']


class StudentsDetailView(LoginRequiredMixin, DetailView):
    model = Students
    context_object_name = 'students'


class EmployeesListView(LoginRequiredMixin, ListView):
    template_name = 'users/employees_list.html'
    model = Employees
    context_object_name = 'employees'
    paginate_by = 10
    queryset = Employees.objects.all().order_by('-created_at')

    def get_queryset(self):
        queryset = Employees.objects.all().order_by('-created_at')
        q = self.request.GET.get('q', '')
        if q:
            queryset = queryset.filter(Q(name__icontains=q))
        elif self.request.GET.get('is_active') == 'True':
            queryset = queryset.filter(is_active=1)
        elif self.request.GET.get('is_active') == 'False':
            queryset = queryset.filter(is_active=0)
        return queryset


class EmployeesCreateView(LoginRequiredMixin, CreateView):
    model = Employees
    form_class = EmployeesAddForm


class EmployeesUpdateView(LoginRequiredMixin, UpdateView):
    model = Employees
    template_name_suffix = '_update_form'
    fields = ['is_active', 'name', 'last_name', 'date_of_birth', 'gender',
              'mothers_name', 'fathers_name', 'rg', 'cpf', 'occupation',
              'bag_helped', 'value', 'employees_type', 'civil_status',
              'address', 'number', 'complement', 'neighborhood', 'city',
              'state', 'cep', 'email', 'phone', 'cellphone', 'comments']


class EmployeesDetailView(LoginRequiredMixin, DetailView):
    model = Employees
    context_object_name = 'employees'


donors_list = DonorsListView.as_view()
donors_add = DonorsCreateView.as_view()
donors_update = DonorsUpdateView.as_view()
donors_detail = DonorsDetailView.as_view()
students_list = StudentsListView.as_view()
students_add = StudentsCreateView.as_view()
students_update = StudentsUpdateView.as_view()
students_detail = StudentsDetailView.as_view()
employees_list = EmployeesListView.as_view()
employees_add = EmployeesCreateView.as_view()
employees_update = EmployeesUpdateView.as_view()
employees_detail = EmployeesDetailView.as_view()
