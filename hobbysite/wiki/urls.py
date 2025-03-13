from django.urls import path
from .views import ArticleList, ArticleDetail

urlpatterns = [
    path('wiki/articles/', ArticleList.as_view(), name = 'article_list'),
    path('wiki/article/<int:pk>/', ArticleDetail.as_view(), name = 'article_detail')
]

app_name = 'wiki'