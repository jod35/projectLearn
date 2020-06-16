from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib import messages

# Create your views here.


def index(request):
    return render(request, 'blog/index.html')


def signup(request):
    form = UserRegisterForm()

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()

            messages.success(
                request, 'Your account has been Created successfully, Please Login')
            return redirect('blog:login')

    context = {
        'form': form,
        'message': messages
    }
    return render(request, 'blog/signup.html', context)
