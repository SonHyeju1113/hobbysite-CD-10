from django.contrib import admin
from .models import Thread, ThreadCategory, Comment

class ThreadAdmin(admin.ModelAdmin):
    model = Thread

class ThreadCategoryAdmin(admin.ModelAdmin):
    model = ThreadCategory

class CommentAdmin(admin.ModelAdmin):
    model = Comment

admin.site.register(Thread, ThreadAdmin)
admin.site.register(ThreadCategory, ThreadCategoryAdmin)
admin.site.register(Comment, CommentAdmin)