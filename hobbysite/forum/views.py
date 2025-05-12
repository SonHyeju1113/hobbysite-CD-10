from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormMixin
from .models import Thread, ThreadCategory, Comment
from .forms import ThreadCreateForm, ThreadUpdateForm, CommentForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse

class ThreadListView(ListView):
    model = ThreadCategory
    template_name = 'thread_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        other_threads_by_category = {}
        if user.is_authenticated and hasattr(user, 'profile'):
            profile = user.profile
            context['my_threads'] = Thread.objects.filter(author = self.request.user.profile)
            
            for category in ThreadCategory.objects.all():
                threads = Thread.objects.filter(category = category).exclude(author = profile)
                if threads.exists():
                    other_threads_by_category[category] = threads
        else:
            context['my_threads'] = []
            
            for category in ThreadCategory.objects.all():
                threads = Thread.objects.filter(category = category)
                if threads.exists():
                    other_threads_by_category[category] = threads
        context['other_threads_by_category'] = other_threads_by_category
        return context

class ThreadDetailView(FormMixin, DetailView):
    model = Thread
    template_name = 'thread_detail.html'
    form_class = CommentForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_thread = self.object
        context['other_threads'] = Thread.objects.filter(
            category = current_thread.category).exclude(pk = current_thread.pk)[:2]
        context['form'] = self.get_form()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        
        if form.is_valid():
            comment = form.save(commit = False)
            comment.thread = self.object
            comment.author = self.request.user.profile
            comment.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
    
    def get_success_url(self):
        return reverse('forum:thread_detail', args = [self.object.pk])

class ThreadCreateView(LoginRequiredMixin, CreateView):
    model = Thread
    form_class = ThreadCreateForm
    template_name = 'thread_create.html'
    redirect_field_name = 'thread_detail'

    def form_valid(self, form):
        form.instance.author = self.request.user.profile
        return super().form_valid(form)

class ThreadUpdateView(LoginRequiredMixin, UpdateView):
    model = Thread
    form_class = ThreadUpdateForm
    template_name = 'thread_update.html'

    def get_success_url(self):
        return reverse('forum:thread_detail', args = [self.object.pk])