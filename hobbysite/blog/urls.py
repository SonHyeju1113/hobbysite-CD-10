from django.urls import path
from .views import blog_list, blog_article

urlpatterns = [
    path('blog/articles', blog_list, name='blog_list'),
    path('blog/article/1', blog_article, name='blog_article'),
]
