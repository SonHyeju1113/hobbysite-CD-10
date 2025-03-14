from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Product, ProductType

class ProductListView(ListView):
    """
    List View class that uses the model Product from models.py
    """
    model = Product
    template_name = 'product_list.html'
    context_object_name = 'product_types' 

    def get_queryset(self):
        """
        To avoid displaying repetiting product types in the list view.
        """
        return ProductType.objects.prefetch_related('product_type')  

class ProductDetailView(DetailView):
    """
    Detailed View class that uses the model Product from models.py
    """
    model = Product
    template_name = 'product_entry.html'