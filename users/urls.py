# coding=utf-8
from django.conf.urls import url
from users import views

urlpatterns = [
    url(r'^doadores/$', views.donors_list, name='donors_list'),
    url(r'^adicionar-doador/$', views.donors_add, name='donors_add'),
    url(r'^detalhes-doador/(?P<pk>[\w_-]+)/$', views.donors_detail,
        name='donors_detail'),
    url(r'^editar-doador/(?P<pk>[\w_-]+)/$', views.donors_update,
        name='donors_update'),
]
