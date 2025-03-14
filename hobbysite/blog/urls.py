"""
@brief Url paths for Blog app.
"""
from django.urls import path
from .views import ArticleListView, ArticleDetailView

urlpatterns = [
    path('blog/articles/', ArticleListView.as_view(), name='articles'),
    path('blog/article/<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
]
