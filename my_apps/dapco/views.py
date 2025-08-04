from django.shortcuts import render, redirect
from .models import *

# Create your views here.

def index(request):
    return render(request, 'dapco/index.html')


def not_found_view(request):
    return render(request, 'dapco/not_found.html')


def encuestas_view(request):
    
    usuario = request.user
    user = CustomUser.objects.get(user=usuario)
    
    encuestas = PermisosEncuestas.objects.filter(usuario=user)
    
    
    context = {
        'encuestas':encuestas,
    }

    return render(request, 'dapco/encuestas.html', context)



def encuesta_detail_view(request, encuesta_id):
    
    usuario = request.user
    user = CustomUser.objects.get(user=usuario)
    try:
        encuesta = PermisosEncuestas.objects.get(id=encuesta_id, usuario=user).encuesta
    except PermisosEncuestas.DoesNotExist:
        encuesta = None
    except Exception as e:
        encuesta = None
    
    # Si la encuesta no existe o el usuario no tiene permiso, redirigir o mostrar un error
    if not encuesta or encuesta == None:
        return redirect('dapco:not_found')
    
    
    conteo = encuesta.conteo_distribuciones_vs_respuestas()
    
    
    context = {
        'encuesta': encuesta,
        'conteo': conteo,
    }
    
    return render(request, 'dapco/encuesta_detail.html', context)


def cuotas_encuesta_view(request, encuesta_id):
    es_htmx = request.headers.get("HX-Request") == "true"
    edad = request.GET.get('edad')
    sexo = request.GET.get('sexo')
    barrio = request.GET.get('barrio')
    estrato = request.GET.get('estrato')
    
    
    usuario = request.user
    user = CustomUser.objects.get(user=usuario)
    try:
        encuesta = PermisosEncuestas.objects.get(id=encuesta_id, usuario=user).encuesta
    except PermisosEncuestas.DoesNotExist:
        encuesta = None
    except Exception as e:
        encuesta = None
        
    context = {
        'encuesta': encuesta,
    }
    
    # Si la encuesta no existe o el usuario no tiene permiso, redirigir o mostrar un error
    if not encuesta or encuesta == None:
        return redirect('dapco:not_found')
    
    if not es_htmx:
        edades = Distribucion.objects.filter(encuesta=encuesta).values_list('edad', flat=True).distinct()
        context['edades'] = edades
        return render(request, 'dapco/encuesta_cuotas.html', context)
    
    if not edad and not sexo and not barrio:
        edades = Distribucion.objects.filter(encuesta=encuesta).values_list('edad', flat=True).distinct()
        context['edades'] = edades
        return render(request, 'dapco/partials/_edades.html', context)

    # Caso 2: eligió edad -> mostrar géneros
    if edad and not sexo:
        sexos = Distribucion.objects.filter(encuesta=encuesta, edad=edad).values_list('sexo', flat=True).distinct()
        context['sexos'] = sexos
        context['edad'] = edad
        return render(request, 'dapco/partials/_sexos.html', context)

    # Caso 3: eligió edad y género -> mostrar barrios
    if edad and sexo and not barrio:
        barrios = Distribucion.objects.filter(encuesta=encuesta, edad=edad, sexo=sexo).values_list('barrio', flat=True).distinct()
        context['barrios'] = barrios
        context['edad'] = edad
        context['sexo'] = sexo
        return render(request, 'dapco/partials/_barrios.html', context)

    # Caso 4: eligió edad y género y barrios -> mostrar estrato
    if edad and sexo and barrio:
        estratos = Distribucion.objects.filter(encuesta=encuesta,edad=edad, sexo=sexo, barrio=barrio).values_list('barrio', flat=True).distinct()
        
        context['estratos'] = estratos
        context['edad'] = edad
        context['sexo'] = sexo
        context['barrio'] = barrio
        
        return render(request, 'dapco/partials/_resumen.html', context)
        
    # Caso 5: eligió todo -> mostrar resumen/final
    if edad and sexo and barrio:
        cuota = Distribucion.objects.filter(encuesta=encuesta, edad=edad, sexo=sexo, barrio=barrio, estrato=estrato).first()
        context['estrato'] = estrato
        context['cuota'] = cuota
        context['edad'] = edad
        context['sexo'] = sexo
        context['barrio'] = barrio
        
        return render(request, 'encuestas/partials/_resumen.html', context)
    
    