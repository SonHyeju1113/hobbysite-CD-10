"""
@brief Admin module for Blog app.
"""
from django.contrib import admin
from .models import Article, ArticleCategory, Comment, Gallery

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

class CommentAdmin(admin.ModelAdmin):
    """
    @brief Instantiates Comment model to CommentAdmin class
    """
    model = Comment

class GalleryAdmin(admin.ModelAdmin):
    """
    @brief Instantiates Gallery model to GalleryAdmin class
    """
    model = Gallery

admin.site.register(Article, ArticleAdmin)
admin.site.register(ArticleCategory, ArticleCategoryAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Gallery, GalleryAdmin)
