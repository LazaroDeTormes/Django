from django.urls import path
from . import views
urlpatterns = [
    path('', views.information, name='information'),
    path('cliente/new', views.cliente_new, name='cliente_new'),
    path('torneos', views.torneos, name='torneos'),
    path('tienda', views.tienda, name='tienda'),
]