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
    posts = Post.objects.filter(author=user_id).order_by('city')
    form = Profile_Form(instance=user)
    return render(req, 'user/profile.html', {'user': user, 'posts': posts, 'form': form})

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
