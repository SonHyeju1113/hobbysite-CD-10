from django.db import models
from django.urls import reverse

# Create your models here.
class ProductType(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=False)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']
        verbose_name_plural = "Product Types"

class Product(models.Model):
    name = models.CharField(max_length=255)
    product_type = models.ForeignKey(ProductType, on_delete=models.SET_NULL, null=True, related_name = "product_type")
    description = models.TextField(blank=False)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('merchstore:product_detail', args=[str(self.pk)])
    
    class Meta:
        ordering = ['name']