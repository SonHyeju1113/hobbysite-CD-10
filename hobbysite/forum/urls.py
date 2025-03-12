from django.urls import path
from .views import PostListView, PostDetailView

urlpatterns = [
    path('forum/threads', PostListView.as_view(), name = 'post_detail'), 
    path('forum/thread/<int:pk>', PostDetailView.as_view(), name = 'post_detail'),
]