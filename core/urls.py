from django.conf.urls import url, include
from core import views

urlpatterns = [
    url(r'^$', views.IndexView, name='index'),
]
