from django.contrib import admin
from .models import Commission, Comment

class CommissionAdmin(admin.ModelAdmin):
    model = Commission

class CommentAdmin(admin.ModelAdmin):
    model = Comment