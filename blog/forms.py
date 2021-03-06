from .models import Post,Comment,Profile
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class PostCreationForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('tags','title', 'body', 'status')


class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=('body',)

        
class BioCreationForm(forms.ModelForm):

    class Meta:
        model=Profile
        fields=['bio',]