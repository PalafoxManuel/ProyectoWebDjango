from django.shortcuts import render

# Create your views here.
def busqueda(request):
    context = {}
    return render(request, 'TiendaBien/busqueda.html', context)

def carrito(request):
    context = {}
    return render(request, 'TiendaBien/carrito.html', context)

def configU(request):
    context={}
    return render(request, 'TiendaBien/configU.html', context)

def historialCompra(request):
    context={}
    return render(request, 'TiendaBien/historialCompra.html', context)

def inicio(request):
    context={}
    return render(request, 'TiendaBien/Inicio.html', context)

def InicioSesion(request):
    context={}
    return render(request, 'TiendaBien/InicioSesion.html', context)

def InicioSesionIniciada(request):
    context={}
    return render(request, 'TiendaBien/InicioSesionIniciada.html', context)

def Registro(request):
    context={}
    return render(request, 'TiendaBien/Registro.html', context)

def verCascos(request):
    context={}
    return render(request, 'TiendaBien/ver-productoCASCOSNEGROS.html', context)

def verRedmi(request):
    context={}
    return render(request, 'TiendaBien/ver-productoREDMI.html', context)

def verSkull(request):
    context={}
    return render(request, 'TiendaBien/ver-productoSKULLCANDY.html', context)

def InicioSesion(request):
    context={}
    return render(request, 'TiendaBien/InicioSesion.html', context)