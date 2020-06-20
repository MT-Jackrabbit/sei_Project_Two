from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('user/', views.on_login, name='on_login'),
    path('user/<int:user_id>', views.user_profile, name='profile'),
    path('accounts/signup', views.sign_up, name='signup'),
    path('accounts/login', views.login, name="login"),
    path('user/<int:user_id>/edit', views.user_edit, name='edit'),
    path('user/<int:post_id>/show_post', views.show_post, name='show_post'),
    path('', views.login, name="login")
]