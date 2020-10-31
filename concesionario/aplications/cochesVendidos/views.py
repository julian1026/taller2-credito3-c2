from django.shortcuts import render

from django.views.generic import TemplateView, ListView,CreateView,UpdateView
from .models import CochesVendidos

# Create your views here.

class CochesCreateView(CreateView):
    template_name = "addVehiculos.html"
    model=CochesVendidos
    fields=('__all__')
    success_url= '.'

class CochesUpdate(UpdateView):
    template_name = "actualizar1.html"
    model=CochesVendidos
    fields=('__all__')
    success_url='/mostrarClientes'

    # success_url= reverse_lazy('home_app:correcto')
  