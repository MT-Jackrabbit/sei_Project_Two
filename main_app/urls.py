from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('user/<int:user_id>', views.user_profile, name='profile'),
    path('accounts/signup', views.sign_up, name='signup'),
    path('accounts/login', views.login, name="login"),
    path('user/<int:user_id>/edit', views.user_edit, name='edit'),
    path('', views.login, name="login")
]