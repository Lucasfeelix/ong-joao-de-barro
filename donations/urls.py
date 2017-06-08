from django.conf.urls import url, include
from donations import views

urlpatterns = [
    url(r'^$', views.donations, name='donation'),
    url(r'^adicionar/$', views.donations_add, name='donation_add'),
    url(r'^detalhes/(?P<pk>[\w_-]+)/$', views.donations_detail,
        name='donation_detail'),
    url(r'^editar/(?P<slug>[\w_-]+)/$', views.donations_update,
        name='donation_update'),
]
