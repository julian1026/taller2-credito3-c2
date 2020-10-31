from django.contrib import admin
from django.urls import path

from.import views
urlpatterns = [
    path('addRevisiones/', views.RevisionesCreateView.as_view()),
    path('mostrarRevisiones/', views.MostrarRevisiones.as_view()),
    path('UpdateRevisiones/<pk>/', views.RevisionesUpdate.as_view()),
]

