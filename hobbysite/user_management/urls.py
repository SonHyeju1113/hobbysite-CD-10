from django.urls import path
from .views import RegisterView, ProfileView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('accounts/profile/', ProfileView.as_view(), name='profile'),
]
