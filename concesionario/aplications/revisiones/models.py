from django.db import models
from aplications.cochesVendidos.models import CochesVendidos

# Create your models here.
class Revisiones (models.Model):
    n_revision = models.IntegerField()
    cambio_aceite = models.BooleanField(default=False)
    cambio_filtro = models.BooleanField(default=False)
    revision_frenos = models.BooleanField(default=False)
    Otros = models.CharField(max_length= 100)
    matricula= models.ForeignKey(CochesVendidos, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.n_revision)
