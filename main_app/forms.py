from django.forms import ModelForm
from .models import UserProfile, Post

class Profile_Form(ModelForm):
    class Meta:
        model = UserProfile
        fields = ['name', 'city', 'imageURL']


class Post_Form(ModelForm):
    class Meta: 
        model = Post
        fields = ['title', 'content', 'city', 'author']