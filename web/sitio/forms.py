from django import forms
from .models import *

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['dni','nombre','fecha_alta','direccion','mobile']


class NoticiaForm(forms.ModelForm):
    class Meta:
        model = Noticia
        fields = ['imagen','titular','previsualizacion','cuerpo','fecha']

class TorneoForm(forms.ModelForm):
    class Meta:
        model = Torneo
        fields = ['titulo','descripcion','requisitos','fecha_tor_emp','fecha_tor_fin']