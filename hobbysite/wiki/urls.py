from django.urls import path
from .views import ArticleList, ArticleDetail, ArticleCreate, ArticleUpdate

urlpatterns = [
    path('articles/', ArticleList.as_view(), name = 'article_list'),
    path('article/<int:pk>/', ArticleDetail.as_view(), name = 'article_detail'),
    path('article/add/', ArticleCreate.as_view(), name = "article_create"),
    path('article/<int:pk>/edit', ArticleUpdate.as_view(), name = "article_update"),
]

app_name = 'wiki'