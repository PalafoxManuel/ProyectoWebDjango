from django.shortcuts import render, redirect
from django.db import connection
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

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

def registrarUsuario(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        correo = request.POST['correo']
        telefono = request.POST['telefono']
        direccion = request.POST['direccion']
        contra = request.POST['contra']

        try:
            user = User.objects.create_user(
                    username=correo,
                    email=correo,
                    first_name=nombre,
                    password=contra,
                    last_name=apellido)
            user.save()
            login(request, user)
            return redirect('InicioSesionIniciada') 

        except Exception as e:
            # Manejo de errores
            print(f'Error al crear el usuario: {str(e)}')
            messages.error(request, f'Error al crear el usuario: {str(e)}')

    # Si no es una solicitud POST, simplemente renderiza la página de registro
    context = {}
    return render(request, 'TiendaBien/Registro.html', context)

def ISU(request):
    if request.method == 'POST':
        correo = request.POST['correo']
        contrasena = request.POST['contrasena']
        
        print(f'Correo: {correo}, Contraseña: {contrasena}')
        
        try:
            user = authenticate(request, username=correo, password=contrasena)

            if user is not None:
                print('Usuario autenticado') 
                login(request, user)
                messages.success(request, 'Inicio de sesión exitoso.')
                return redirect('InicioSesionIniciada')
            else:
                print('Credenciales incorrectas') 
                messages.error(request, 'Correo o contraseña incorrectos.')
                return render(request, 'TiendaBien/InicioSesion.html')
        except Exception as e:
            print(f'Error al iniciar sesión: {str(e)}')
            messages.error(request, 'Error al iniciar sesión.')
    elif request.method == "GET":
        return render(request, 'TiendaBien/InicioSesion.html')
    

    