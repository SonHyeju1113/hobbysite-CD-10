from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Article

# Create your views here.
class ArticleList(ListView):
    model = Article

class ArticleDetail(DetailView):
    model = Article