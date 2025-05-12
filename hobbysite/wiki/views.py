from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from .models import Article

class ArticleList(ListView):
    model = Article
    template_name = 'wiki_list.html'

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Article.objects.exclude(author=self.request.user)
        return super().get_queryset()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.request.user.is_authenticated:
            user_articles = Article.objects.filter(author=self.request.user)
            context['user_articles'] = user_articles
        return context

class ArticleDetail(DetailView):
    model = Article
    template_name = 'wiki_detail.html'

class ArticleCreate(CreateView):
    model = Article
    template_name = 'wiki_create.html'
    fields = ['title', 'category', 'entry', 'header_image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self):
        return super().get_success_url()
    
    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)

class ArticleUpdate(UpdateView):
    model = Article
    template_name = 'wiki_update.html'