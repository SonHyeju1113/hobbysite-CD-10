from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Comment

class CommentListView(ListView):
    model = Comment
    template_name = 'comment_list.html'