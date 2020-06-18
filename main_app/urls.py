from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('user/<int:user_id>', views.user_profile, name='profile'),
    path('', views.login, name="login")
]