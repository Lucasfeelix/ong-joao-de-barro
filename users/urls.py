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
    url(r'^alunos/$', views.students_list, name='students_list'),
    url(r'^adicionar-aluno/$', views.students_add, name='students_add'),
    url(r'^detalhes-aluno/(?P<pk>[\w_-]+)/$', views.students_detail,
        name='students_detail'),
    url(r'^editar-aluno/(?P<pk>[\w_-]+)/$', views.students_update,
        name='students_update'),
]
