from django import forms
from django.forms import inlineformset_factory, modelformset_factory
from .models import Thread, ThreadCategory, Comment

class ThreadCreateForm(forms.ModelForm):
    class Meta:
        model = Thread
        fields = ['title', 'category', 'entry']

class ThreadUpdateForm(forms.ModelForm):
    class Meta:
        model = Thread
        fields = ['title', 'category', 'entry']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['entry']