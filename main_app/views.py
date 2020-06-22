from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import UserProfile, Post, City
from .forms import Profile_Form, Post_Form

# Create your views here.
def home(req):
    forms = {'logInForm': AuthenticationForm(), 'signUpForm': UserCreationForm(), 'profileForm': Profile_Form()}
    return render(req, 'home.html', forms)

# --- on_login redirect route --- #
def on_login(req):
    form = AuthenticationForm(data = req.POST)
    if form.is_valid():
        username = req.POST.get('username')
        password = req.POST.get('password')
        user = authenticate(username=username, password=password)
        login(req, user)
        profile = UserProfile.objects.get(user=user.id)
        return redirect('profile', profile.id)
    else:
        context = {'logInForm': form, 'signUpForm': UserCreationForm(), 'profileForm': Profile_Form(), 'errors': form.errors}
        return render(req, 'home.html', context )

# --- user_profile route --- #
def user_profile(req, user_id):
    profile = UserProfile.objects.get(id=user_id)
    print(f"Profile return = {profile}")
    
    if(req.GET.get("sort") == 'asc'):
        posts = Post.objects.filter(author=user_id).order_by( '-city__name')
    elif(req.GET.get("sort") == 'desc'):
        posts = Post.objects.filter(author=user_id).order_by('city__name')
    else:
        posts = Post.objects.filter(author=user_id)

    form = Profile_Form(instance=profile)
    return render(req, 'user/profile.html', {'profile': profile, 'posts': posts, 'form': form})

# --- user_edit route --- #
def user_edit(req, user_id):
    user = UserProfile.objects.get(id=user_id)
    if req.method == "POST":
        form = Profile_Form(req.POST, instance=user)
        if form.is_valid():
            print(form)
            form.save()
            return redirect('profile', user_id=user_id)
    else:
        form = Profile_Form(instance=user)
    
    return render(req, 'user/profile.html', {'user': user, 'form': form})

# --- show_post route --- #
def show_post(req, post_id):
    post = Post.objects.get(id=post_id)
    context = {'post': post}
    return render(req, 'user/show_post.html', context)

# --- add_post route --- #
def add_post(req):
    if req.method == 'POST':
        city = City.objects.get(id = req.POST['cityId'])
        user = User.objects.get(id = req.POST['userId'])
        profile = UserProfile.objects.get(user = req.user.id)
        post = Post(title = req.POST['title'],content = req.POST['content'], author = profile, city = city, user = user)
        post.save()
        return redirect('cities', city_id = city.id)
    else:
        return redirect('home')

# --- del_post route --- #
@login_required
def del_post(req, post_id):
    Post.objects.get(id=post_id).delete()
    return redirect('cities')

# --- edit_post route --- #
def edit_post(req, post_id):
    print(req.POST)
    if req.method == 'POST':
        city = City.objects.get(id = req.POST['city'])
        user = User.objects.get(id = req.POST['user'])
        profile = UserProfile.objects.get(user_id = req.POST['user'])
        post= Post.objects.get(id = post_id)
        post_form = Post_Form(req.POST, instance = post)
        post_form.save()
        return redirect('cities', city_id = city.id)
    else:
        return redirect('home')

# --- city_posts route --- #
def city_posts(req, city_id):
    post_form = Post_Form(data ={'city': city_id})
    cities = City.objects.all().order_by('name')
    city = City.objects.get(id=city_id)
    posts = Post.objects.filter(city_id=city_id)
    return render(req, 'cities/city_profile.html', {'city': city, 'cities': cities, 'posts': posts, 'postForm': post_form})


######## Admin Routes ########

# --- sign_up route --- #
def sign_up(req):
    err_message = ''
    if req.method == 'POST':
        user_form = UserCreationForm(data = {'username' : req.POST['username'], 'password1' : req.POST['password1'], 'password2' : req.POST['password2']})
        profile_form = Profile_Form(data = {'name' : req.POST['name'], 'city' : req.POST['city']})
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile_form = Profile_Form(data = {'name' : req.POST['name'], 'city' : req.POST['city']})
            new_form = profile_form.save(commit = False)
            new_form.user_id = user.id
            login(req, user)
            new_form.save()
            #using the profile id so that this
            profile = UserProfile.objects.get(user=user.id)
            return redirect('profile', profile.id)
        else:
            context = {'signUpForm': user_form, 'profileForm': profile_form, 'errors': user_form.errors}
            print(context)
            return render(req, 'home.html', context )




