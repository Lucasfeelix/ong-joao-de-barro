from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model


User = get_user_model()


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'index.html'


index = IndexView.as_view()
