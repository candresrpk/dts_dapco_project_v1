from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class CustomUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cargo = models.CharField(max_length=100)
    
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'usuario'
        verbose_name_plural = 'usuarios'
    
    def __str__(self):
        return f'{self.user}'


class Encuesta(models.Model):
    administrador = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)    
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'encuesta'
        verbose_name_plural = 'encuestas'

    def __str__(self):
        return f'Encuesta: {self.nombre} - creada por {self.administrador}'


class PermisosEncuestas(models.Model):
    usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    encuesta = models.ForeignKey(Encuesta, on_delete=models.CASCADE)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'permiso'
        verbose_name_plural = 'permisos'
        
    def __str__(self):
        return f'{self.encuesta} - {self.usuario}'
    

class Distribucion(models.Model):
    edad = models.IntegerField()
    sexo = models.CharField(max_length=1)
    barrio = models.CharField(max_length=3)
    estrato = models.IntegerField()
    
    usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    encuesta = models.ForeignKey(Encuesta, on_delete=models.CASCADE)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'distribucion'
        verbose_name_plural = 'distribuciones'
    
    def __str__(self):
        return f'{self.edad} - {self.sexo} - {self.barrio} - {self.estrato}'
    

class Pregunta(models.Model):
    
    class TipoChoiches(models.TextChoices):
        Abierta = 'Abierta'
        Opciones = 'Opciones'
    
    pregunta = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100, choices=TipoChoiches.choices, default=TipoChoiches.Opciones)
    encuesta = models.ForeignKey(Encuesta, on_delete=models.CASCADE)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'pregunta'
        verbose_name_plural = 'preguntas'
    
    def __str__(self):
        return f'{self.pregunta}'
    

class Opcion(models.Model):
    opcion = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='opciones', null=True, blank=True)
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    class Meta:
        verbose_name = 'opcion'
        verbose_name_plural = 'opciones'
    
    def __str__(self):
        return f'{self.opcion}'
    

class Respuesta(models.Model):
    
    encuestador = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)    
    opcion = models.ForeignKey(Opcion, on_delete=models.CASCADE)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'respuesta'
        verbose_name_plural = 'respuestas'
    
    def __str__(self):
        return f'{self.pregunta} respuesta {self.opcion}'