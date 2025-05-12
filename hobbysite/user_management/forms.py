from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import Profile

#Used Django's built in Register Form https://www.youtube.com/watch?v=tUqUdu0Sjyc&t=679s
class UserRegisterForm(UserCreationForm):
    display_name = forms.CharField(max_length=63, required=True)
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'display_name', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)

        user.username = self.cleaned_data['username']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()
            Profile.objects.create(
                user=user,
                display_name=self.cleaned_data['display_name'],
                email=self.cleaned_data['email']
            )
        return user

class UserEditProfile(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['display_name', 'email']
