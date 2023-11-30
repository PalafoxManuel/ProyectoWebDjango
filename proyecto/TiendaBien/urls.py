from django.urls import path
from . import views


urlpatterns = [
    path('busqueda/', views.busqueda, name='busqueda'),
    '''path('carrito/', carrito, name='carrito'),
    path('configU/', configU, name='configU'),
    path('historialCompra/', historialCompra, name='historialCompra'),
    path('Inicio/', inicio, name='Inicio'),
    path('InicioSesion/', InicioSesion, name='InicioSesion'),
    path('InicioSesionIniciada/', InicioSesionIniciada, name='InicioSesionIniciada'),
    path('Registro/', Registro, name='Registro'),
    path('ver-productoCASCOSNEGROS/', verCascos, name='verCascos'),
    path('ver-productoREDMI/', verRedmi, name='verRedmi'),
    path('ver-productoSKULLCANDY/', verSkull, name='verSkull')'''
]
