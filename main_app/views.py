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
    form = Profile_Form()
    return render(req, 'user/profile.html', {'user': user, 'form': form})

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

    
