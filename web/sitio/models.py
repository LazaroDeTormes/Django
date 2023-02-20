import datetime

from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class Noticia(models.Model):
    imagen = models.ImageField(upload_to="static/media")
    titular = models.CharField(max_length=15, primary_key= True)
    previsualizacion = models.CharField(max_length=150, blank= False, null = False)
    cuerpo = models.CharField(max_length=500, blank= False, null = False)
    fecha = models.DateTimeField("Noticia a ", blank= False, null = False)

class Torneo(models.Model):
    titulo = models.CharField(max_length=20, primary_key= True)
    descripcion = models.CharField(max_length=200, blank= False, null = False)
    requisitos = models.CharField(max_length=100, blank= False, null = False)
    fecha_tor_emp = models.DateTimeField("Fecha de inicio", blank= False, null = False, default=datetime.datetime.now())
    fecha_tor_fin = models.DateTimeField("Fecha de finiquito", blank=False, null=False, default=datetime.datetime.now())
    concursantes = models.ManyToManyField(User,
                                       related_name='usuarios',
                                    null=True,
                                       blank=True)

class Articulo(models.Model):
    img = models.ImageField(upload_to="static/media")
    nombre = models.CharField(max_length=20, primary_key=True)
    descripcion = models.CharField(max_length=200, blank=False, null=False)
    precio = models.CharField(max_length=100, blank=False, null=False)
    fecha_venta = models.DateTimeField("Fecha de venta", blank=False, null=False, default=datetime.datetime.now())