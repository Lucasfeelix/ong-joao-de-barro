# coding=utf-8
from django.conf.urls import url
from users import views

urlpatterns = [
    url(r'^$', views.donors, name='donors'),
    url(r'^adicionar-doador/$', views.donors_add, name='donors_add'),
    url(r'^detalhes-doador/(?P<pk>[\w_-]+)/$', views.donors_detail,
        name='donors_detail')
]
