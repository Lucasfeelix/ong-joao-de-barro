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
    url(r'^funcionarios/$', views.employees_list, name='employees_list'),
    url(r'^adicionar-funcionario/$', views.employees_add,
        name='employees_add'),
    url(r'^detalhes-funcionario/(?P<pk>[\w_-]+)/$', views.employees_detail,
        name='employees_detail'),
    url(r'^editar-funcionario/(?P<pk>[\w_-]+)/$', views.employees_update,
        name='employees_update'),
]
