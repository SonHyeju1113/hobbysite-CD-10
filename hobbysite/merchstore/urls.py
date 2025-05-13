from django.urls import path
from .views import merchList, merchDetail, merchCreate, merchUpdate, merchCart, merchTransactions


urlpatterns = [
    path('items/', merchList, name='merchstore_list'),
    path('item/<int:pk>/', merchDetail, name='merchstore_detail'),
    path('item/add', merchCreate, name='merchstore_create'),
    path('item/<int:pk>/edit', merchUpdate, name = 'merchstore_update'),
    path('cart/', merchCart, name='merchstore_cart'),
    path('transactions/', merchTransactions, name ='merchstore_transaction'),
]

app_name = "merchstore"