from django.conf.urls import url
from . import views          
urlpatterns = [
    url(r'^$', views.index),
    url(r'^(?P<id>\d+)/process$', views.show_add),
    url(r'^(?P<id>\d+)/add$', views.add),
    url(r'^(?P<id>\d+)/show$', views.show),
    url(r'^(?P<id>\d+)/join$', views.join),
  ]