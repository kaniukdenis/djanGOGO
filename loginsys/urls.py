# coding: utf-8

from django.conf.urls import url
from loginsys import views

urlpatterns = [
    url(r'^signin/$', views.login), 
    url(r'^signout/$', views.logout), 
    url(r'^signup/$', views.register), 
]