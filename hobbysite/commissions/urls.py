from django.urls import path
from .views import CommentListView, CommentDetailView

urlpatterns = [
    path('list/', CommentListView.as_view(), name = 'comment_list'), 
    path('detail/<int:pk>/', CommentDetailView.as_view(), name = 'comment_detail'),
]

app_name = "commissions"