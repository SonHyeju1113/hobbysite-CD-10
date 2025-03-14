from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Product, ProductType

class ProductListView(ListView):
    model = Product
    template_name = 'product_list.html'
    context_object_name = 'product_types' 

    def get_queryset(self):
        return ProductType.objects.prefetch_related('product_type')  

class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_entry.html'