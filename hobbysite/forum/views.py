from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Thread, ThreadCategory

class ThreadListView(ListView):
    model = ThreadCategory
    template_name = 'thread_list.html'

class ThreadDetailView(DetailView):
    model = Thread
    template_name = 'thread_detail.html'