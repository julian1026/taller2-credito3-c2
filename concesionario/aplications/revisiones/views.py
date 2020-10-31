from django.shortcuts import render

from django.views.generic import TemplateView, ListView,CreateView,UpdateView
from .models import Revisiones

# Create your views here.

class RevisionesCreateView(CreateView):
    template_name = "addRevisiones.html"
    model=Revisiones
    fields=('__all__')
    success_url= '.'

class MostrarRevisiones(ListView):
    template_name = "Mrevisiones.html"
    model=Revisiones
    context_object_name='listar'

class RevisionesUpdate(UpdateView):
    template_name = "actualizar2.html"
    model=Revisiones
    fields=('__all__')
    success_url='/mostrarRevisiones'

    # success_url= reverse_lazy('home_app:correcto')
  