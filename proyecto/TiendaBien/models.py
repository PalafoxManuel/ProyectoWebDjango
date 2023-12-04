from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User
from django.contrib.auth.models import User as AuthUser, UserManager

# Create your models here.
        
class Producto(models.Model):
    stock = models.IntegerField(validators=[MinValueValidator(0)])
    descuento = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    precioDescuento = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    nombre = models.CharField(max_length=255, null=False)
    urlimagen = models.CharField(max_length=255, null=False)
    precio = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    estrellas = models.PositiveIntegerField(null=False)
    descripcion = models.TextField( null=False,blank=False)
    isDeleted = models.BooleanField(null=False)
    
    class Meta:
        db_table = 'producto'
        
class Categoria(models.Model):
    nombreCategoria = models.CharField(max_length=255, null=False, blank=False)
    
    class Meta:
        db_table = 'categoria'
    
    
class ProductoCategoria(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.PROTECT)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)

    class Meta:
        db_table= 'productoCategoria'
        
class Usuario(models.Model):
    nombre = models.CharField(max_length=255, null=False, blank=False)
    apellido = models.CharField(max_length=255, null=False, blank=False)
    correo = models.EmailField(unique=True, null=False, blank=False)
    telefono = models.CharField(max_length=50, null=True, blank=True)
    direccion = models.CharField(max_length=1000, null=True, blank=True)
    contrasena = models.CharField(max_length=255, null=False, blank=False)

    class Meta:
        db_table = 'usuario'

class Opiniones(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    estrellas = models.IntegerField()
    titulo = models.CharField(max_length=255)
    comentario = models.TextField()

    class Meta:
        db_table = 'opiniones'
        


class Carrito(models.Model):
    idCarrito = models.BigAutoField(primary_key=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    class Meta:
        db_table = 'carrito'

class DetalleCarrito(models.Model):
    carrito = models.ForeignKey(Carrito, on_delete=models.DO_NOTHING)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField(validators=[MinValueValidator(0)])
    precioUnitario = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'detalleCarrito'

class HistorialCompras(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING)
    fechaCompra = models.DateTimeField()
    montoTotal = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    class Meta:
        db_table = 'historialCompras'



class DetalleCompra(models.Model):
    compra = models.ForeignKey(HistorialCompras, on_delete=models.DO_NOTHING)
    urlimagen = models.CharField(max_length=255)
    nombre = models.CharField(max_length=255)
    cantidad = models.IntegerField()
    precioUnitario = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'detalleCompra'

class User(AuthUser):
    class Meta:
        db_table = 'user'

    telefono = models.CharField(max_length=50, null=True, blank=True)
    direccion = models.CharField(max_length=1000, null=True, blank=True)

    objects = UserManager()
                