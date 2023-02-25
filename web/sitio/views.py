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





def joinTournament(request):
    if request.method == "POST":

        titulo = request.POST.get('titulo')
        tournamentId = titulo
        user = request.user
        print(titulo)
        tournament = Torneo.objects.get(titulo=tournamentId)
        tournament.concursantes.add(user)
        return redirect('torneos')
    else:
        return render(request, 'toeneos.html')



def sobreNos(request):
    return render(request, 'sitio/sobrenosotros.html')

def clientes(request, titulo):
    torneo = Torneo.objects.get(titulo=titulo)

    concursantes = torneo.concursantes.all()

    return render(request, 'sitio/concursantes.html', {'torneo': torneo, 'concursantes': concursantes})



def torneos(request):
    torneos = Torneo.objects.filter(fecha_tor_emp__lte=timezone.now()).order_by('fecha_tor_emp')
    return render(request, 'sitio/torneos.html',{'torneos':torneos})

def tienda(request):
    tienda = Articulo.objects.filter(fecha_venta__lte=timezone.now()).order_by('fecha_venta')
    return render(request, 'sitio/tienda.html',{'tienda':tienda})



class Login(LoginView):
    template_name = 'sitio/login.html'
    fields = '__all__'
    redirect_authenticated_user = False

    def get_success_url(self):
        return reverse_lazy('torneos')

class Registro(FormView):
    template_name = 'sitio/registro.html'
    form_class = UserCreationForm
    redirect_authenticated_user = False
    success_url = reverse_lazy('registro')

    def form_valid(self, form):
        usuario = form.save()
        if usuario is not None:
            login(self.request, usuario)
        return super(Registro, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('torneos')
