"""
@brief Class-Based Views for Blog app.
"""
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from .models import Article, ArticleCategory
from .forms import ArticleCreateForm

class ArticleListView(LoginRequiredMixin,ListView):
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

class ArticleCreateView(CreateView):
    model = Article
    form_class = ArticleCreateForm
    template_name = 'blog_create.html'
    success_url = reverse_lazy('articles')
