"""
@brief Url paths for Blog app.
"""
from django.urls import path
from .views import ArticleListView, ArticleDetailView, ArticleCreateView, ArticleUpdateView

urlpatterns = [
    path('blog/articles/', ArticleListView.as_view(), name='articles'),
    path('blog/article/<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
    path('blog/create/', ArticleCreateView.as_view(), name='article_create'),
    path('blog/update/<int:pk>/', ArticleUpdateView.as_view(), name='article_update'),
]
