from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Post, PostCategory

class PostListView(ListView):
    model = PostCategory
    template_name = 'forum_list.html'

class PostDetailView(DetailView):
    model = Post
    template_name = 'forum_entry.html'