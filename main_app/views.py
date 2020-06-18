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


