from django.shortcuts import render
##
from django.urls import reverse_lazy

from django.views.generic import TemplateView, ListView,CreateView,UpdateView
from .models import Clientes
from aplications.cochesVendidos.models  import CochesVendidos
# Create your views here.




class PruebaCreateView(CreateView):
    template_name = "add.html"
    model=Clientes
    fields=('__all__')
    success_url= '.'

class MostrarClientes(ListView):
    coche=CochesVendidos.objects.prefetch_related()
    template_name = "Fclientes.html"
    context_object_name = 'listar'
    queryset = coche
    fields = ('_all_')

class ClienteUpdate(UpdateView):
    template_name = "actualizar.html"
    model=Clientes
    fields=('__all__')
    success_url='/mostrarClientes'
  