from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
def home(req):
    return render(req, 'home.html')

def users_profile(req):
    return render(req, 'users/profile.html')