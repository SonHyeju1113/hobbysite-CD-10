from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Thread, ThreadCategory, Comment
from .forms import ThreadCreateForm, ThreadUpdateForm, CommentForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.urls import reverse

class ThreadListView(ListView):
    model = ThreadCategory
    template_name = 'thread_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user

        if user.is_authenticated:
            context['my_threads'] = Thread.objects.filter(author = self.request.user.profile)
            context['other_threads'] = Thread.objects.exclude(author = self.request.user.profile)
        else:
            context['my_threads'] = []
            context['other_threads'] = Thread.objects.all()

        return context

class ThreadDetailView(DetailView):
    model = Thread
    template_name = 'thread_detail.html'
    form_class = Commentform

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
            comment.author = self.user.profile
            comment.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
    
    def get_success_url(self):
        return reverse('thread_detail', kwargs = {'pk:' self.object.pk})

class ThreadCreateView(LoginRequiredMixin, CreateView):
    model = Thread
    form_class = ThreadCreateForm
    template_name = 'thread_create.html'
    redirect_field_name = 'thread_detail'

    def form_valid(self, form):
        form.instance.author = self.request.user.profile
        return super().form_valid(form)

class ThreadUpdateView(LoginRequiredMixin, CreateView):
    model = Thread
    form_class = ThreadCreateForm
    template_name = 'thread_update.html'
    redirect_field_name = 'profile/'

    def get_queryset(self):
        return Thread.objects.filter(author = self.request.user)