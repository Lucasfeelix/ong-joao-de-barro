from django.conf.urls import url, include
from expenses import views

urlpatterns = [
    url(r'^$', views.expenses, name='expense'),
    url(r'^adicionar/$', views.expenses_add, name='expense_add'),
    url(r'^detalhes/(?P<pk>[\w_-]+)/$', views.expenses_detail,
        name='expense_detail')
]
