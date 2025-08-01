from django.shortcuts import render
from .models import *

# Create your views here.

def index(request):
    return render(request, 'dapco/index.html')


def encuestas_view(request):
    
    usuario = request.user
    user = CustomUser.objects.get(user=usuario)
    
    encuestas = PermisosEncuestas.objects.filter(usuario=user)
    
    
    context = {
        'encuestas':encuestas,
    }

    return render(request, 'dapco/encuestas.html', context)