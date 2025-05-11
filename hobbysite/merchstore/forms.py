from django import forms
from .models import ProductType, Product, Transaction

class ProductTypeForm(forms.ModelForm):
    class Meta:
        model = ProductType
        fields = '__all__'