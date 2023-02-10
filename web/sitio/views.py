from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from .forms import *
from .models import *
from django.utils import timezone
def clientes_list(request):
    clientes = Cliente.objects.filter(fecha_alta__lte=timezone.now()).order_by('fecha_alta')
    return render(request, 'sitio/clientes_list.html', {'clientes': clientes})


def information(request):
    noticias = Noticia.objects.filter(fecha__lte=timezone.now()).order_by('fecha')
    return render(request, 'sitio/information.html',{'noticias':noticias})


def cliente_new(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            cliente = form.save()
            cliente.save()
    else:
        form = ClienteForm()
    return render(request, 'sitio/cliente_new.html',{'form': form})

def login(request):
    if request.method == 'POST':
        username = request.POST['nombre']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            # El usuario no se autenticó correctamente
            return render(request, 'sitio/login.html', {'error': 'Nombre de usuario o contraseña incorrectos'})
    else:
        # Mostrar formulario de inicio de sesión
        return render(request, 'sitio/login.html')


def torneos(request):
    torneos = Torneo.objects.filter(fecha_tor_emp__lte=timezone.now()).order_by('fecha_tor_emp')
    return render(request, 'sitio/torneos.html',{'torneos':torneos})

def tienda(request):
    tienda = Articulo.objects.filter(fecha_venta__lte=timezone.now()).order_by('fecha_venta')
    return render(request, 'sitio/tienda.html',{'tienda':tienda})