"""
@brief Admin module for Blog app.
"""
from django.contrib import admin
from .models import Article, ArticleCategory

class ArticleAdmin(admin.ModelAdmin):
    """
    @brief Instantiates Article model to ArticleAdmin class
    """
    model = Article

class ArticleCategoryAdmin(admin.ModelAdmin):
    """
    @brief Instantiates ArticleCategory model to ArticleCategoryAdmin class
    """
    model = ArticleCategory

admin.site.register(Article, ArticleAdmin)
admin.site.register(ArticleCategory, ArticleCategoryAdmin)
