from django.contrib import admin
from django.urls import path

from.import views
app_name="cliente_app"
urlpatterns = [
    path('mostrarClientes/', views.MostrarClientes.as_view()),
    path('addClientes/', views.PruebaCreateView.as_view()),
    path('UpdateClientes/<pk>/', views.ClienteUpdate.as_view()),
]
