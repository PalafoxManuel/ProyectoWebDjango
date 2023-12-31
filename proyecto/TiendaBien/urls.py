from django.urls import path
from . import views


urlpatterns = [
    path('registrarUsuario/', views.registrarUsuario, name='registrarUsuario'),
    path('busqueda/', views.busqueda, name='busqueda'),
    path('carrito/', views.carrito, name='carrito'),
    path('configU/', views.configU, name='configU'),
    path('historialCompra/', views.historialCompra, name='historialCompra'),
    path('Inicio/', views.inicio, name='Inicio'),
    path('InicioSesion/', views.ISU, name='InicioSesion'),
    path('InicioSesionIniciada/', views.InicioSesionIniciada, name='InicioSesionIniciada'),
    path('Registro/', views.Registro, name='Registro'),
    path('ver-producto/', views.verProducto, name='verProducto'),

    path('categoria/<str:nombre_categoria>/', views.productos_por_categoria, name='productos_por_categoria'),

]