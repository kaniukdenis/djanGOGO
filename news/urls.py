"""news URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,patterns, include
from django.contrib import admin
from news.views import index
from django.conf.urls.static import static
from public import views
from django.conf import settings

urlpatterns = [

    url(r'^$', index),
    url(r'^admin/', admin.site.urls),
    url(r'^allnews/$',views.spisok),
    url(r'^mainnews/$', views.mainnews),
    url(r'^mainnews/(?P<public_id>\d+)/$', views.detail),
    url(r'^science/$',views.science),
    url(r'^science/(?P<public_id>\d+)/$', views.detail),
    url(r'^science/likes/(?P<public_id>\d+)/$', views.addlikes),
    url(r'^science/dislikes/(?P<public_id>\d+)/$', views.adddislikes),
    url(r'^science/addcomment/(?P<public_id>\d+)/$', views.addcomment),
    
    url(r'^society/$',views.society),
    url(r'^society/(?P<public_id>\d+)/$', views.detail),
    
    url(r'^bussiness/$',views.bussiness),
    url(r'^bussiness/(?P<public_id>\d+)/$', views.detail),
    url(r'^policy/$',views.policy),
    url(r'^policy/(?P<public_id>\d+)/$', views.detail),
    url(r'^culture/$',views.culture),
    url(r'^culture/(?P<public_id>\d+)/$', views.detail),
    
    

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
