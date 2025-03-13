from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Product

class ProductListView(ListView):
    model = Product
    template_name = 'product_list.html'