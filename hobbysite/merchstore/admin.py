from django.contrib import admin
from .models import ProductType, Product

class ProductTypeAdmin(admin.ModelAdmin):
    """
    Instantiates ProductType model to ProductTypeAdmin class
    """
    model = ProductType
    list_display = ('name', 'description')
    ordering = ['name']

class ProductAdmin(admin.ModelAdmin):
    """
    Instantiates Product model to ProductAdmin class
    """
    model = Product
    list_display = ('product_type', 'name', 'price', 'description',)
    ordering = ['name']

admin.site.register(ProductType, ProductTypeAdmin)
admin.site.register(Product, ProductAdmin)
