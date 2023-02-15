from django.urls import path
from . import views
from .views import Login, Registro

urlpatterns = [
    path('', views.information, name='information'),
    path('registro', Registro.as_view, name='registro'),
    path('login', Login.as_view, name='login'),
    path('torneos', views.torneos, name='torneos'),
    path('tienda', views.tienda, name='tienda'),
]