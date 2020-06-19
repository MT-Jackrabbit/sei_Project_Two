from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required

from .models import UserProfile, Post
from .forms import Profile_Form, Post_Form

# Create your views here.
def home(req):
    forms = {'logInForm': AuthenticationForm(), 'signUpForm': UserCreationForm()}
    return render(req, 'home.html', forms)

def user_profile(req, user_id):
    user = UserProfile.objects.get(id=user_id)
    
    if(req.GET.get("sort") == 'asc'):
        posts = Post.objects.filter(author=user_id).order_by('-city')
    elif(req.GET.get("sort") == 'desc'):
        posts = Post.objects.filter(author=user_id).order_by('city')
    else:
        posts = Post.objects.filter(author=user_id)
    
    form = Profile_Form(instance=user)
    return render(req, 'user/profile.html', {'user': user, 'posts': posts, 'form': form})


def show_post(req, post_id):
    post = Post.objects.get(id=post_id)
    context = {'post': post}
    return render(req, 'user/show_post.html', context)

def sign_up(req):
    err_message = ''
    if req.method == 'POST':
        form = UserCreationForm(req.POST)
        if form.is_valid():
            user = form.save()
            login(req, user)
            return redirect('home')
        else:
            context = {'signUpForm': form, 'errors': form.errors}
            print(context['errors'])
            return render(req, 'home.html', context )

""" def log_in(req):
    if req.method == 'POST':
        form == AuthenticationForm(req.POST)
        if form.is_valid() == False:
            context = {'logInForm': form, 'errors': form.errors}
            return render('home', context ) """

def user_edit(req, user_id):
    user = UserProfile.objects.get(id=user_id)
    if req.method == "POST":
        form = Profile_Form(req.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile', user_id=user_id)
    else:
        form = Profile_Form(instance=user)
    
    return render(req, 'user/profile.html', {'user': user, 'form': form})

