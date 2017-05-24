from django.conf.urls import url, include
from donations import views

urlpatterns = [
    url(r'^$', views.IndexView, name='index'),
]
