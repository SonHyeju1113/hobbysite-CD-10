from django import forms
from .models import Article, Comment

class ArticleCreateForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'category', 'entry', 'header_image']

class ArticleCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['entry']
