from django.contrib import admin
from article.models import Article

# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'publication_date')
    search_fields = ('title',)
    list_filter = ('title',)

admin.site.register(Article, ArticleAdmin)
