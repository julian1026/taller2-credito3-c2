from django.db import models

#importanto llave foranea
from aplications.clientes.models import Clientes


# Create your models here.

class CochesVendidos(models.Model):
    matricula=models.CharField(max_length=100)
    marca=models.CharField(max_length=50)
    modelo=models.CharField(max_length=100)
    color=models.CharField(max_length=50)
    precio=models.FloatField()
    extras_instalados=models.CharField(max_length=50)
    numero_puertas=models.IntegerField()
    codigo_cliente=models.ForeignKey(Clientes, on_delete=models.CASCADE)

    def __str__(self):
        return self.matricula

