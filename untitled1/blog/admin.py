from django.contrib import admin

from .models import Article, Category, Tag


class ArticlePostAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'category')


#

admin.site.register(Article, ArticlePostAdmin)

admin.site.register(Category)

admin.site.register(Tag)
