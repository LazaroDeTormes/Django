from django import forms
from .models import *




class NoticiaForm(forms.ModelForm):
    class Meta:
        model = Noticia
        fields = ['imagen','titular','previsualizacion','cuerpo','fecha']

class TorneoForm(forms.ModelForm):
    class Meta:
        model = Torneo
        fields = ['titulo','descripcion','requisitos','fecha_tor_emp','fecha_tor_fin']

class TiendaForm(forms.ModelForm):
    class Meta:
        model = Articulo
        fields = ['img','nombre','descripcion','precio', 'fecha_venta']