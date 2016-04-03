from django.conf.urls import url,patterns, include
from django.contrib import admin
from news.views import index
from django.conf.urls.static import static
from public import views
from django.conf import settings

urlpatterns = [

    url(r'^allnews/$',views.spisok),
    url(r'^mainnews/$', views.mainnews),
    url(r'^mainnews/(?P<public_id>\d+)/$', views.detail),

    url(r'^likes/(?P<public_id>\d+)/$', views.addlikes),
    url(r'^dislikes/(?P<public_id>\d+)/$', views.adddislikes),
    url(r'^science/addcomment/(?P<public_id>\d+)/$', views.addcomment),
    
    url(r'^science/$', views.theme, {'theme': 'Science'}),
    url(r'^science/(?P<public_id>\d+)/$', views.detail),

    url(r'^society/$', views.theme, {'theme': 'Society'}),
    url(r'^society/(?P<public_id>\d+)/$', views.detail),
    
    url(r'^bussiness/$', views.theme, {'theme': 'Bussiness'}),
    url(r'^bussiness/(?P<public_id>\d+)/$', views.detail),

    url(r'^policy/$', views.theme, {'theme': 'Policy'}),
    url(r'^policy/(?P<public_id>\d+)/$', views.detail),

    url(r'^culture/$', views.theme, {'theme': 'Culture'}),
    url(r'^culture/(?P<public_id>\d+)/$', views.detail),
]