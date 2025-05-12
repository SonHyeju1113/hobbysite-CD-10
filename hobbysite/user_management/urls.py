from django.urls import path
from .views import register_view, profile_view, profile_update, home_view

urlpatterns = [
    path('register/', register_view, name='register'),
    path('accounts/profile/', profile_view, name='profile'),
    path('accounts/update/', profile_update, name='profile_update'),
    path('home', home_view, name='home_view')
]
