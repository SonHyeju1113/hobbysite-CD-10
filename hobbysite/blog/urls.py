from django.urls import path
from .views import ArticleListView, ArticleDetailView

urlpatterns = [
    path('blog/articles', ArticleListView.as_view(), name='blog_list'),
    path('blog/article/<int:id>', ArticleDetailView.as_view(), name='blog_article'),
]
