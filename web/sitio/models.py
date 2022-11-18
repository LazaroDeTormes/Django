import datetime

from django.db import models

# Create your models here.
class Cliente(models.Model):
    dni = models.CharField(max_length=8, primary_key= True)
    nombre = models.CharField(max_length=150, blank= False, null = False)
    fecha_alta = models.DateTimeField("Fecha de alta", blank= False, null = False)
    direccion = models.CharField(max_length=150, blank= False, null = True)
    mobile = models.CharField(max_length=150, blank = False, null = True)


class Noticia(models.Model):
    imagen = models.ImageField(upload_to="sitio/static/media")
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