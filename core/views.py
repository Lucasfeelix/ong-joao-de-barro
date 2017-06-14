from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model


User = get_user_model()


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'index.html'


class RegisterCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'register.html'
    success_url = reverse_lazy('index')


index = IndexView.as_view()
register = RegisterCreateView.as_view()
