from django.urls import path
from .views import ProductListView, ProductDetailView

urlpatterns = [
    path('merchstore/items/', ProductListView.as_view(), name='product_list'),
    path('merchstore/item/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
]

app_name = "merchstore"