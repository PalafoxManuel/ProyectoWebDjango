from django.db import models

# Create your models here.
class Carrito(models.Model):
    id_carrito = models.IntegerField()
    estado = models.CharField(max_length=50)

    class Meta:
        db_table= 'carrito'