from django.contrib import admin
from .models import Article

class ArticleInline(admin.TabularInline):
    model = Article
