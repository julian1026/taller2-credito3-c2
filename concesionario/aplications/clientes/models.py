from django.db import models

# Create your models here.

class Clientes(models.Model):
    codigo_cliente=models.CharField(max_length=100)
    nombre_cliente=models.CharField(max_length=50)
    apellido_cliente=models.CharField(max_length=100)
    direccion_cliente=models.CharField(max_length=50)
    poblacion=models.CharField(max_length=100)
    codigo_Postal=models.IntegerField()
    provincia=models.CharField(max_length=100)
    telefono=models.CharField(max_length=50)
    fecha_nacimiento=models.CharField(max_length=100)
    def __str__(self):
        return self.codigo_cliente