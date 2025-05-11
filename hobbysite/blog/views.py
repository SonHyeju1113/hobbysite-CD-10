"""
@brief Class-Based Views for Blog app.
"""
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from .models import Article, ArticleCategory
from .forms import ArticleCreateForm, ArticleCommentForm

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
    context_object_name = "article"

    def get_success_url(self):
        return self.request.path

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ArticleCommentForm()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = ArticleCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = self.object
            comment.author = request.user.profile
            comment.save()
            return self.get(request, *args, **kwargs)
        else:
            self.object_list = self.get_queryset(**kwargs)
            context = self.get_context_data(**kwargs)
            context['form'] = form
            return self.render_to_response(context)

class ArticleCreateView(CreateView):
    model = Article
    form_class = ArticleCreateForm
    template_name = 'blog_create.html'
    success_url = reverse_lazy('articles')
    
    def form_valid(self, form):
        form.instance.author = self.request.user.profile
        return super().form_valid(form)

class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    model = Article
    form_class = ArticleCreateForm
    template_name = 'blog_update.html'
    success_url = reverse_lazy('articles')
