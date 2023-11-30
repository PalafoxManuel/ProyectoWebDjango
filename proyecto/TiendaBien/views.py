from django.shortcuts import render

# Create your views here.
def busqueda(request):
    context = {}
    return render(request, 'TiendaBien/busqueda.html', context)

'''def carrito(request):
    return render(request, 'carrito.html')

def configU(request):
    return render(request, 'configU.html')

def historialCompra(request):
    return render(request, 'historialCompra.html')

def inicio(request):
    return render(request, 'Inicio.html')

def InicioSesion(request):
    return render(request, 'InicioSesion.html')

def InicioSesionIniciada(request):
    return render(request, 'InicioSesionIniciada.html')

def Registro(request):
    return render(request, 'Registro.html')

def verCascos(request):
    return render(request, 'ver-productoCASCOSNEGROS.html')

def verRedmi(request):
    return render(request, 'ver-productoREDMI.html')

def verSkull(request):
    return render(request, 'ver-productoSKULLCANDY.html')

def InicioSesion(request):
    return render(request, 'InicioSesion.html')'''