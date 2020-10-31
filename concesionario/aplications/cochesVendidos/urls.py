from django.contrib import admin
from django.urls import path

from.import views
urlpatterns = [
    path('addCoches/', views.CochesCreateView.as_view()),
    path('UpdateCoches/<pk>/', views.CochesUpdate.as_view()),
]
