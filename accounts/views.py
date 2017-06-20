# coding=utf-8
from django.shortcuts import render
from django.views.generic import CreateView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.models import User
from accounts.forms import UserAdminCreationForm


class RegisterCreateView(LoginRequiredMixin, CreateView):
    model = User
    form_class = UserAdminCreationForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('index')


register = RegisterCreateView.as_view()
