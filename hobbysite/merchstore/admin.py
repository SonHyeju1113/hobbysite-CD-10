from django.contrib import admin
from .models import ProductType, Product

class ProductTypeAdmin(admin.ModelAdmin):
    model = ProductType
    list_display = ('name', 'description')
    ordering = ['name']

class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = ('product_type', 'name', 'price', 'description',)
    ordering = ['name']

