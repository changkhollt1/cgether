from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index),
    path('cuoi_corner', views.cuoicorner),
    path('about', views.about),
    path('register_user', views.register_user, name='register_user'),
    path('login', auth_views.LoginView.as_view(template_name='html/login.html') , name='login'),
    path('logout', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
]
