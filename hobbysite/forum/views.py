from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Thread, ThreadCategory
from .forms import ThreadCreateForm, ThreadUpdateForm

class ThreadListView(ListView):
    model = ThreadCategory
    template_name = 'thread_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user

        if user.is_authenticated:
            context['my_threads'] = Thread.objects.filter(author = user)
            context['other_threads'] = Thread.objects.exclude(author = user)
        else:
            context['my_threads'] = []
            context['other_threads'] = Thread.objects.all()

        return context

class ThreadDetailView(DetailView):
    model = Thread
    template_name = 'thread_detail.html'

class ThreadCreateView(LoginRequiredMixin, CreateView):
    model = Thread
    form_class = ThreadCreateForm
    template_name = 'thread_create.html'
    redirect_field_name = 'profile/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class ThreadUpdateView(LoginRequiredMixin, CreateView):
    model = Thread
    form_class = ThreadCreateForm
    template_name = 'thread_update.html'
    redirect_field_name = 'profile/'

    def get_queryset(self):
        return Thread.objects.filter(author = self.request.user)