from django.urls import path
from . import views  

urlpatterns = [
    path('', views.login, name='login'),  
    path('login/', views.user_login, name='user_login'),  
    path('register/', views.register, name='register'),  
    path('logout/', views.user_logout, name='logout'),  
]
