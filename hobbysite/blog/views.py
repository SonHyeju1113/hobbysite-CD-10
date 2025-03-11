from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Article

class ArticleListView(ListView):
    model = Article
    template_name = 'blog_list.html'

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'blog_article.html'
