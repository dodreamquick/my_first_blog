from django.urls import path
from . import views


urlpatterns = [
    path('', views.post_list, name="post_list"),
    path('post/<int:pk>/', views.post_detail,name="post_detail"), 
    path('post/write/', views.post_write, name="post_write"),
    path('user/login/', views.user_login, name="user_login"),
    path('user/logout', views.user_logout, name="user_logout"),
    path('user/signup',views.user_signup,name="user_signup"),
]