"""
@brief Class-Based Views for Blog app.
"""
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView
from django.http import Http404
from django.urls import reverse_lazy
from .models import Article, ArticleCategory
from .forms import ArticleCreateForm, ArticleCommentForm

class ArticleListView(ListView):
    """
    @brief List View class that uses the model ArticleCategory from models.py
    """
    model = ArticleCategory
    template_name = 'blog_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            user_profile = self.request.user.profile
            context['my_articles'] = Article.objects.filter(author=user_profile)
        return context

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
        current_article = self.get_object()
        context = super().get_context_data(**kwargs)
        context['form'] = ArticleCommentForm()
        context['other_articles'] = Article.objects.filter(
            author=current_article.author).exclude(pk=current_article.pk)
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

class ArticleCreateView(LoginRequiredMixin, CreateView):
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

    def get_object(self, queryset=None):
        article = super().get_object(queryset)
        # Check if the logged-in user is the owner of the article
        if article.author != self.request.user.profile:
            raise Http404("You are not authorized to edit this article.") 
        return article
