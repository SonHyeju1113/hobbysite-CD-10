"""
@brief Url paths for Blog app using Function-Based Views.
"""
from django.urls import path
from .views import article_list_view, article_detail_view, article_create_view, article_update_view

urlpatterns = [
    path('articles/', article_list_view, name='articles'),
    path('article/<int:pk>/', article_detail_view, name='article_detail'),
    path('create/', article_create_view, name='article_create'),
    path('update/<int:pk>/', article_update_view, name='article_update'),
]
