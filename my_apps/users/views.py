from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from ..dapco.models import CustomUser
# Create your views here.


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dapco:encuestas')
            else:
                messages.error(request, "Error en el inicio de sesión. Por favor, verifica tus credenciales.")
        else:
            messages.error(request, "Error en el inicio de sesión. Por favor, verifica tus credenciales.")
    else:\
        form = AuthenticationForm()
    return render(request, 'usuarios/login.html', {'form': form})



def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            customer_user = CustomUser.objects.create(user=user, cargo="Encuestador")
            customer_user.save()
            login(request, user)
            messages.success(request, "Registro exitoso. ¡Bienvenido!")
            return redirect('dapco:encuestas')
        else:
            messages.error(request, "Error en el registro. Por favor, verifica los campos.")
    else:
        form = UserCreationForm()
    return render(request, 'usuarios/singup.html', {'form': form})



def logout_view(request):
    logout(request)
    return redirect('dapco:index')