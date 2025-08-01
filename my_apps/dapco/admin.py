from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('user', 'cargo')
    

@admin.register(Encuesta)
class EncuestaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'administrador')
    search_fields = ('nombre', 'administrador__username')
    

@admin.register(PermisosEncuestas)
class PermisosEncuestasAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'encuesta')
    search_fields = ('usuario__user__username', 'encuesta__nombre')


@admin.register(Distribucion)
class DistribucionAdmin(admin.ModelAdmin):
    list_display = ('edad', 'sexo', 'barrio', 'estrato', 'usuario', 'encuesta')
    search_fields = ('usuario__user__username', 'encuesta__nombre', 'barrio')
    list_filter = ('sexo', 'estrato')
    ordering = ('edad', 'sexo', 'barrio')
    readonly_fields = ('created_at', 'updated_at')

@admin.register(Pregunta)
class PreguntaAdmin(admin.ModelAdmin):
    list_display = ('pregunta', 'tipo', 'encuesta')
    search_fields = ('pregunta', 'encuesta__nombre')
    list_filter = ('tipo', 'encuesta')
    readonly_fields = ('created_at', 'updated_at')
    
    
@admin.register(Opcion)
class OpcionAdmin(admin.ModelAdmin):
    list_display = ('opcion', 'pregunta')
    search_fields = ('opcion', 'pregunta__pregunta')
    list_filter = ('pregunta',)
    readonly_fields = ('created_at', 'updated_at')


@admin.register(Respuesta)
class RespuestaAdmin(admin.ModelAdmin):
    list_display = ('encuestador', 'pregunta', 'opcion')
    search_fields = ('encuestador__user__username', 'pregunta__pregunta', 'opcion__opcion')
    list_filter = ('pregunta', 'opcion')
    readonly_fields = ('created_at', 'updated_at')
