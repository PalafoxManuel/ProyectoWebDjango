from django.urls import path
from . import views


urlpatterns = [
    path('registrarUsuario/', views.registrarUsuario, name='registrarUsuario'),
    path('busqueda/', views.busqueda, name='busqueda'),
    path('carrito/', views.carrito, name='carrito'),
    path('configU/', views.configU, name='configU'),
    path('historialCompra/', views.historialCompra, name='historialCompra'),
    path('Inicio/', views.inicio, name='Inicio'),
    path('InicioSesion/', views.InicioSesion, name='InicioSesion'),
    path('InicioSesionIniciada/', views.InicioSesionIniciada, name='InicioSesionIniciada'),
    path('Registro/', views.Registro, name='Registro'),
    path('ver-productoCASCOSNEGROS/', views.verCascos, name='verCascos'),
    path('ver-productoREDMI/', views.verRedmi, name='verRedmi'),
    path('ver-productoSKULLCANDY/', views.verSkull, name='verSkull')
]
