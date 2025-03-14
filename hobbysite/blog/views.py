"""
@brief Class-Based Views for Blog app.
"""
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Article, ArticleCategory

class ArticleListView(ListView):
    """
    @brief List View class that uses the model ArticleCategory from models.py
    """
    model = ArticleCategory
    template_name = 'blog_list.html'

class ArticleDetailView(DetailView):
    """
    @brief Detail View clas that uses the model Article from models.py
    """
    model = Article
    template_name = 'blog_article.html'
