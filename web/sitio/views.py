from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import FormView

from .forms import *
from .models import *
from django.utils import timezone



def information(request):
    noticias = Noticia.objects.filter(fecha__lte=timezone.now()).order_by('fecha')
    return render(request, 'sitio/information.html',{'noticias':noticias})







def torneos(request):
    torneos = Torneo.objects.filter(fecha_tor_emp__lte=timezone.now()).order_by('fecha_tor_emp')
    return render(request, 'sitio/torneos.html',{'torneos':torneos})

def tienda(request):
    tienda = Articulo.objects.filter(fecha_venta__lte=timezone.now()).order_by('fecha_venta')
    return render(request, 'sitio/tienda.html',{'tienda':tienda})



class Login(LoginView):
    template_name = 'sitio/login.html'
    field = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('torneos')

class Registro(FormView):
    template_name = 'sitio/registro.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('torneos')

    def form_valid(self, form):
        usuario = form.save()
        if usuario is not None:
            login(self.request, usuario)
            return super(Registro, self.form_valid(form))

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('torneos')
        return super(Registro, self).get(*args, **kwargs)