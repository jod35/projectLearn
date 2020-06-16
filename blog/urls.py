from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'blog'


urlpatterns = [
    path('', views.index, name='home'),
    path('signup/', views.signup, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/loggedout.html'), name='loggedout'),

]
