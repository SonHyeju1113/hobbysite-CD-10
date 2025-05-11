from django.contrib import admin
from .models import Thread, ThreadCategory

class ThreadAdmin(admin.ModelAdmin):
    model = Thread

class ThreadCategoryAdmin(admin.ModelAdmin):
    model = ThreadCategory

admin.site.register(Thread, ThreadAdmin)
admin.site.register(ThreadCategory, ThreadCategoryAdmin)