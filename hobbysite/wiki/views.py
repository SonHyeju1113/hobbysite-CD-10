from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Article

# Create your views here.
class ArticleList(ListView):
    model = Article
    template_name = 'wiki_list.html'

class ArticleDetail(DetailView):
    model = Article
    template_name = 'wiki_detail.html'