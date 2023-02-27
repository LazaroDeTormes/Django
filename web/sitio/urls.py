from django.contrib.auth.views import LogoutView
from django.urls import path
from . import views
from .views import Login, Registro

urlpatterns = [
    path('', views.information, name='information'),
    path('registro/', Registro.as_view(), name='registro'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('torneos', views.torneos, name='torneos'),
    path('tienda', views.tienda, name='tienda'),
    path('torneos/<str:titulo>/concursantes/', views.clientes , name='clientes_list'),
    path('inscripcion/', views.joinTournament, name='ins'),
    path('sobreNosotros', views.sobreNos, name='sobreNosotros')
]