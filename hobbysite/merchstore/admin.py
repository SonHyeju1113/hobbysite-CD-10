from django.contrib import admin
from .models import ProductType

class ProductTypeAdmin(admin.ModelAdmin):
    model = ProductType
    list_display = ('name', 'description')
    ordering = ['name']
