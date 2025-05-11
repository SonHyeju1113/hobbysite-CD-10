from django.urls import path
from .views import ThreadListView, ThreadDetailView, ThreadCreateView, ThreadUpdateView

urlpatterns = [
    path('forum/threads/', ThreadListView.as_view(), name = 'thread_list'), 
    path('forum/thread/<int:pk>/', ThreadDetailView.as_view(), name = 'thread_detail'),
    path('forum/thread/add/', ThreadCreateView.as_view(), name = 'thread_create'),
    path('forum/thread/<int:pk>/edit/', ThreadUpdateView.as_view(), name = 'thread_update')
]

app_name = "forum"