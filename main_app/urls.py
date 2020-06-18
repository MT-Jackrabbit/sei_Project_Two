from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('users/<int:user_id>', views.users_profile, name='profile')
]