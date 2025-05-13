from django import forms
from django.forms import inlineformset_factory
from .models import Article, Comment, Gallery

class ArticleCreateForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'category', 'entry', 'header_image']

class ArticleCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['entry']

ArticleGalleryForm = inlineformset_factory(
    Article, Gallery,
    fields=['image', 'description'],
    extra=1,
    can_delete=True
)
