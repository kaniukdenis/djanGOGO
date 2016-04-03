# coding: utf-8

from django.contrib import admin
from public.models import Public

class PublicAdmin(admin.ModelAdmin):
    list_display = ('head','theme', 'date_pub',)
    list_filter = ['date_pub']
    exclude = ('likes', 'dislikes',)
    
admin.site.register(Public, PublicAdmin)

# Register your models here.
