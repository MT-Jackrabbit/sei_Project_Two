from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('user/', views.on_login, name='on_login'),
    path('user/<int:profile_id>', views.user_profile, name='profile'),
    path('user/<int:profile_id>/edit', views.user_edit, name='edit'),
    path('user/add_post', views.add_post, name='add_post'),
    path('user/<int:post_id>/show_post', views.show_post, name='show_post'),
    path('user/<int:post_id>/del_post', views.del_post, name='del_post'),
    path('user/<int:post_id>/edit_post', views.edit_post, name='edit_post'),
    path('cities/<int:city_id>', views.city_posts, name="cities"),
    path('accounts/signup', views.sign_up, name='signup'),
    path('accounts/login', views.login, name="login"),
    path('', views.login, name="login")
]