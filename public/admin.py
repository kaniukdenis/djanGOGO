from django.contrib import admin
from public.models import Public

class PublicAdmin(admin.ModelAdmin):
    list_display = ('head','theme', 'date_pub')
    list_filter = ['date_pub']
    
admin.site.register(Public, PublicAdmin)

# Register your models here.
