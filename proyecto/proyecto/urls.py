from django.contrib import admin
from django.urls import path
from proyecto.vista import busqueda
from proyecto.vista import carrito
from proyecto.vista import configU
from proyecto.vista import historialCompra
from proyecto.vista import inicio
from proyecto.vista import InicioSesion
from proyecto.vista import InicioSesionIniciada
from proyecto.vista import Registro
from proyecto.vista import verCascos
from proyecto.vista import verRedmi
from proyecto.vista import verSkull
from proyecto.vista import InicioSesion

urlpatterns = [
    path('admin/', admin.site.urls),
    path('busqueda/', busqueda, name='busqueda'),
    path('carrito/', carrito, name='carrito'),
    path('configU/', configU, name='configU'),
    path('historialCompra/', historialCompra, name='historialCompra'),
    path('Inicio/', inicio, name='Inicio'),
    path('InicioSesion/', InicioSesion, name='InicioSesion'),
    path('InicioSesionIniciada/', InicioSesionIniciada, name='InicioSesionIniciada'),
    path('Registro/', Registro, name='Registro'),
    path('ver-productoCASCOSNEGROS/', verCascos, name='verCascos'),
    path('ver-productoREDMI/', verRedmi, name='verRedmi'),
    path('ver-productoSKULLCANDY/', verSkull, name='verSkull')
]
