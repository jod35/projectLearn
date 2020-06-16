from django.shortcuts import render
from .forms import UserRegisterForm

# Create your views here.


def index(request):
    return render(request, 'blog/index.html')


def signup(request):
    form = UserRegisterForm()

    context = {
        'form': form
    }
    return render(request, 'blog/signup.html', context)
