from django.shortcuts import render, redirect
from .forms import UserRegisterForm, PostCreationForm
from .models import Post
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.


def index(request):
    posts=Post.objects.all()


    if request.method =="POST":
        form=PostCreationForm(request.POST)

        if form.is_valid():
            form.save(commit=False)
            

            return redirect('blog:home')
    context={
        'posts':posts
    }
    return render(request, 'blog/index.html',context)


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


@login_required
def create_post(request):
    form = PostCreationForm()

    if request.method=='POST':
        form=PostCreationForm(request.POST)

        if form.is_valid():
            obj=form.save(commit=False)
            obj.author=request.user
            obj.save()

            form.save_m2m()
            messages.success(request,'Your Post Is Now Live!')
            return redirect('blog:home')


    context = {
       'form': form
    }
    return render(request, 'blog/createpost.html', context)


