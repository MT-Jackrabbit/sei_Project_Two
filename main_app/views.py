from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import UserProfile, Post
from .forms import Profile_Form, Post_Form

# Create your views here.
def home(req):
    return render(req, 'home.html')

def users_profile(req, user_id):
    user = UserProfile.objects.get(id=user_id)
    # user_form = Profile_form(instance=user)
    return render(req, 'users/profile.html', {'user': user})