from django.db import models
from django.urls import reverse

class ProductType(models.Model):
    """
    Instantiates Product Model and return name. 
    """
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=False)

    def __str__(self):
        return self.name
    
    class Meta:
        """
        To sort the model in ascending order with respect to model name.
        Verbose name to set admin panel name to Product Types.
        """
        ordering = ['name']
        verbose_name = 'Product Type'
        verbose_name_plural = 'Product Types'
        

class Product(models.Model):
    """
    Instantiates Product Model and return name and absolute URL.
    """
    name = models.CharField(max_length=255)
    product_type = models.ForeignKey(ProductType,null=True ,on_delete=models.SET_NULL, related_name='products')
    owner = models.ForeignKey('user_management.Profile',on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    STATUS_CHOICES = (
        ('available', 'Available'),
        ('on_sale', 'On Sale'),
        ('out_of_stock', 'Out of Stock'),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='available')

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name