# coding=utf-8
from django.shortcuts import render
from django.views.generic import CreateView, TemplateView, UpdateView, FormView
from django.views.generic import DetailView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import PasswordChangeForm
from accounts.models import User
from accounts.forms import UserAdminCreationForm


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/index.html'


class UserDetailView(LoginRequiredMixin, DetailView):
    model = User
    context_object_name = 'users'


class RegisterCreateView(LoginRequiredMixin, CreateView):
    model = User
    form_class = UserAdminCreationForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('index')


class UserUpdateView(UpdateView):
    """
    Pode inficar o formulário que ira servir para alteração, deduso eu,
    UserAdminCreationForm
    """
    model = User
    fields = ['name', 'email', 'is_active']
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('accounts:index')

    def get_object(self):
        return self.request.user


class UpdatePasswordView(LoginRequiredMixin, FormView):
    """
    UpdateView: FormView baseado por/para modelo.
    FormView: crua não possui modelo associado.
    """
    template_name = 'accounts/update_password.html'
    success_url = reverse_lazy('accounts:index')
    form_class = PasswordChangeForm

    def get_form_kwargs(self):
        """
        Método que pega/gera argumentos que serão passados para o formulário
        """
        kwargs = super(UpdatePasswordView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.save()
        return super(UpdatePasswordView, self).form_valid(form)


register = RegisterCreateView.as_view()
index = IndexView.as_view()
update_user = UserUpdateView.as_view()
update_password = UpdatePasswordView.as_view()
user_detail = UserDetailView.as_view()
