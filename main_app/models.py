from django.db import models
from django.utils.timesince import timesince

from django.contrib.auth.models import User

# Create your models here.
class City(models.Model):
    name = models.CharField(max_length=100)
    img = models.CharField(max_length=250, default='')

    def __str__(self):
        return self.name

class UserProfile(models.Model):
    name = models.CharField(max_length=100)
    imageURL = models.ImageField(upload_to= 'profile_image', blank = True, default= '')
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    # will create the date and set editable=False and blank=True
    joined_on = models.DateField(auto_now_add=True)
    user = models.OneToOneField(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(max_length=3000)
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.title

    def Time_Since(self):
        return f"Published: {timesince(self.created_on)} ago"