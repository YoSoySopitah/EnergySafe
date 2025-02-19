from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib import messages
from .models import CustomUser

def login(request):
    return render(request, 'core/index.html')

def user_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            auth_login(request, user)
            return redirect("home")
        else:
            try:
                from pymongo import MongoClient
                client = MongoClient('mongodb://localhost:27017/')
                db = client['EnergySafe']
                collection = db['Users']
                
                usuario = collection.find_one({"username": username})
                if usuario:
                    messages.error(request, "El usuario existe pero la contraseña es incorrecta")
                else:
                    messages.error(request, "Usuario o contraseña incorrectos")
            except Exception as e:
                messages.error(request, "Error al intentar iniciar sesión")
            
            return redirect("login")
    
    return render(request, 'core/index.html')

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]
        
        if password1 != password2:
            messages.error(request, "Las contraseñas no coinciden")
            return redirect("register")
        
        if CustomUser.objects.filter(username=username).exists():
            messages.error(request, "El nombre de usuario ya está en uso")
            return redirect("register")
        
        if CustomUser.objects.filter(email=email).exists():
            messages.error(request, "El email ya está registrado")
            return redirect("register")
        
        try:
            user = CustomUser(username=username, email=email)
            user.set_password(password1)
            user.save()
            
            messages.success(request, "Registro exitoso, inicia sesión")
            return redirect("login")
        except Exception as e:
            messages.error(request, f"Error al registrar: {str(e)}")
            return redirect("register")
    
    return render(request, 'core/index.html')

def user_logout(request):
    logout(request)
    return redirect("login")
