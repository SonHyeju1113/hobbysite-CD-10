from django.contrib import admin
from .models import Article, ArticleCategory

# Register your models here.
class ArticleInline(admin.TabularInline):
    model = Article

class ArticleAdmin(admin.ModelAdmin):
    model = Article

    fieldsets = [('Details', {'fields': ['title', 'entry']})]

class ArticleCategoryAdmin(admin.ModelAdmin):
    inlines = [ArticleInline,]

admin.site.register(Article, ArticleAdmin)
admin.site.register(ArticleCategory, ArticleCategoryAdmin)