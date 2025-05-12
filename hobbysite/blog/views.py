"""
@brief Views for Blog app.
"""
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,  get_object_or_404, redirect
from django.http import Http404
from django.urls import reverse_lazy
from .models import Article, ArticleCategory, Gallery
from .forms import ArticleCreateForm, ArticleCommentForm, ArticleGalleryForm

def article_list_view(request):
    """
    @brief View that lists ArticleCategory and adds user-specific articles if authenticated.
    """
    categories = ArticleCategory.objects.all()
    context = {'object_list': categories}

    if request.user.is_authenticated:
        user_profile = request.user.profile
        context['my_articles'] = Article.objects.filter(author=user_profile)

    return render(request, 'blog_list.html', context)

def article_detail_view(request, pk):
    """
    @brief View to display an article and handle comment submission.
    """
    article = get_object_or_404(Article, pk=pk)
    gallery_images = Gallery.objects.filter(article=article)

    if Article.objects.filter(author=article.author
                              ).exclude(pk=article.pk).count() > 1:
        other_articles = Article.objects.filter(author=article.author).exclude(pk=article.pk)
    else:
        other_articles = None

    if request.method == 'POST':
        form = ArticleCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article
            comment.author = request.user.profile
            comment.save()
            form = ArticleCommentForm()
    else:
        form = ArticleCommentForm()

    context = {
        'article': article,
        'form': form,
        'other_articles': other_articles,
        'gallery_images': gallery_images,
    }

    return render(request, 'blog_article.html', context)

@login_required
def article_create_view(request):
    """
    @brief View to handle article creation.
    """
    if request.method == 'POST':
        form = ArticleCreateForm(request.POST, request.FILES)
        formset = ArticleGalleryForm(request.POST, request.FILES)

        if form.is_valid() and formset.is_valid():
            article = form.save(commit=False)
            article.author = request.user.profile
            article.save()

            formset.instance = article
            formset.save()
            return redirect('article_detail', article.pk)
    else:
        form = ArticleCreateForm()
        formset = ArticleGalleryForm()

    return render(request, 'blog_create.html', {'form': form,
                                                'formset' : formset})

@login_required
def article_update_view(request, pk):
    """
    @brief View to update an article and its gallery images. Only the author can edit.
    """
    article = get_object_or_404(Article, pk=pk)

    if article.author != request.user.profile:
        raise Http404("You are not authorized to edit this article.")

    if request.method == 'POST':
        form = ArticleCreateForm(request.POST, request.FILES, instance=article)
        formset = ArticleGalleryForm(request.POST, request.FILES, instance=article)

        if form.is_valid() and formset.is_valid():
            print(formset.cleaned_data) 
            form.save()
            formset.save()
            return redirect('article_detail', pk=article.pk)
    else:
        form = ArticleCreateForm(instance=article)
        formset = ArticleGalleryForm(instance=article)

    return render(request, 'blog_update.html', {'form': form,
                                                'formset': formset,
                                                'article': article})