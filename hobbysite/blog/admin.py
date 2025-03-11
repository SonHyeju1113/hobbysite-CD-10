from django.contrib import admin
from .models import Article, ArticleCategory

class ArticleAdmin(admin.TabularInline):
    model = Article

class ArticleCategoryAdmin(admin.ModelAdmin):
    model = ArticleCategory


