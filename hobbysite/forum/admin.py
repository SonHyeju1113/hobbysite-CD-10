from django.contrib import admin
from .models import Post, PostCategory

class PostAdmin(admin.ModelAdmin):
    model = Post

class PostCategoryAdmin(admin.ModelAdmin):
    model = PostCategory

admin.site.register(Post, PostAdmin)
admin.site.register(PostCategory, PostCategoryAdmin)