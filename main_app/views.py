from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required

from .models import UserProfile, Post
from .forms import Profile_Form, Post_Form

# Create your views here.
def home(req):
    forms = {'logInForm': AuthenticationForm(), 'signUpForm': UserCreationForm(), 'profileForm': Profile_Form()}
    return render(req, 'home.html', forms)

def user_profile(req, user_id):
    user = UserProfile.objects.get(user =user_id)
    form = Profile_Form()
    posts = Post.objects.filter(author=user_id).order_by('city')
    form = Profile_Form(instance=user)
    return render(req, 'user/profile.html', {'user': user, 'posts': posts, 'form': form})

def show_post(req, post_id):
    post = Post.objects.get(id=post_id)
    context = {'post': post}
    return render(req, 'user/show_post.html', context)

def sign_up(req):
    err_message = ''
    if req.method == 'POST':
        user_form = UserCreationForm(data = {'username' : req.POST['username'], 'password1' : req.POST['password1'], 'password2' : req.POST['password2']})
        if user_form.is_valid():
            user = user_form.save()
            profile_form = Profile_Form(data = {'name' : req.POST['name'], 'city' : req.POST['city']})
            new_form = profile_form.save(commit = False)
            new_form.user_id = user.id
            login(req, user)
            new_form.save()
            return redirect(f'../user/{user.id}')
        else:
            print('forms invalid')
            profile_form = Profile_Form(data = {'name' : req.POST['name'], 'city' : req.POST['city']})
            # context = {'signUpForm': user_form , 'profileForm': profile_form}
            # return render(req, 'home.html', context )

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

