from django.urls import path
from .views import ArticleList, ArticleDetail

urlpatterns = [
    path('articles/', ArticleList.as_view(), name = 'article_list'),
    path('article/<int:pk>/', ArticleDetail.as_view(), name = 'article_detail')
]

app_name = 'wiki'