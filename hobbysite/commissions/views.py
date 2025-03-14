from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Comment, Commission

class CommentListView(ListView):
    model = Commission
    template_name = 'comment_list.html'
    context_object_name = 'commissions'

class CommentDetailView(DetailView):
    model = Commission
    template_name = 'comment_entry.html'
    
    def get_context_data(self, **args):
        context = super().get_context_data(**args)
        context['comments'] = Comment.objects.filter(commission=self.object)
        return context