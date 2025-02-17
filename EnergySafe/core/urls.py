from django.urls import path
from . import views  # Importa el archivo views.py

urlpatterns = [
    path('', views.login, name='login'),  # Ruta de login
]
