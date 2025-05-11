from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

from .forms import UserRegisterForm

def register_view(request):
    """
    @brief Function-Based View for user registration.
    """
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})

@login_required
def profile_view(request):
    """
    @brief Function-Based View for displaying the user's profile.
    """
    return render(request, 'profile.html')