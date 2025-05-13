from django.contrib import admin
from .models import Article, ArticleCategory

class ArticleInline(admin.TabularInline):
    model = Article

class ArticleAdmin(admin.ModelAdmin):
    model = Article

    search_fields = ('title', 'created_on', 'updated_on',)
    list_display = ('title', 'created_on', 'updated_on',)
    list_filter = ('title', 'created_on', 'updated_on',)

    fieldsets = [('Details', {'fields': ['title', 'entry']})]

class ArticleCategoryAdmin(admin.ModelAdmin):
    inlines = [ArticleInline,]

    search_fields = ('name',)
    list_display = ('name',)
    list_filter = ('name',)

admin.site.register(Article, ArticleAdmin)
admin.site.register(ArticleCategory, ArticleCategoryAdmin)