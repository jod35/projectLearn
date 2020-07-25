from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'blog'


urlpatterns = [
    path('', views.index, name='home'),
    path('signup/', views.signup, name='register'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/loggedout.html'), name='logout'),
    path('create_post',views.create_post,name='add_post'),
    path('posts/<str:title>/',views.post_details,name='post_details'),
    path('update_post/<pk>/',views.PostUpdateView.as_view(),name='update_post'),
    path('user_profile/<str:username>/',views.user_profile,name='user_profile'),

]
