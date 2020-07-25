from django.shortcuts import render, redirect
from .forms import UserRegisterForm, PostCreationForm,CommentForm,BioCreationForm
from .models import Post,Comment,Profile
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import UpdateView
from django.contrib.auth.models import User

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


#page for an individual post

@login_required
def post_details(request,title):

    post=Post.objects.get(title=title)
    comments=Comment.objects.filter(author=request.user).order_by('-commented_on')
    form=CommentForm()

    if request.method =='POST':
        form=CommentForm(request.POST)

        if form.is_valid():
            obj=form.save(commit=False)

            obj.author=request.user
            obj.post=post

            obj.save()

            return redirect(f'/posts/{post.title}')


    context={
        'post':post,
        'form':form,
        'comments':comments
    }
    return render(request,'blog/post_detail.html',context)


class PostUpdateView(UpdateView):
    model=Post
    template_name='blog/updatepost.html'
    success_url='/'
    fields=['title','body']


def user_profile(request,username):

    user=User.objects.filter(username=username).first()
    posts=Post.objects.filter(author=user).all()[:4]
    
    for post in posts:
        comments=Comment.objects.filter(post=post).order_by('-commented_on')

    context={
        'posts':posts,
        'user':user,
        'comments':comments
    }
    return render(request,'blog/profile.html',context)


# class BioUpdateView(UpdateView):
#     model=Profile
#     template_name='blog/updatebio.html'
#     fields=['bio']
#     success_url='/'


def create_user_bio(request):
    form=BioCreationForm()

    if request.method == 'POST':
        form=BioCreationForm(request.POST)

        if form.is_valid():
            obj=form.save(commit=False)
            obj.user=request.user

            obj.save()

            return redirect('/user_profile/{}'.format(request.user.username))


    context={
        'form':form
    }
    return render(request,'blog/createbio.html',context)



class ProfileUpdateView(UpdateView):
    template_name='blog/updatebio.html'
    model=Profile
    success_url='/'
    fields=['bio']