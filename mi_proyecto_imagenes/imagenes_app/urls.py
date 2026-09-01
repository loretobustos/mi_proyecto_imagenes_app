from django.urls import path
from . import views

urlpatterns = [
    path('subir/', views.subir_imagen, name='subir_imagen'),
    path('mostrar/', views.mostrar_imagenes, name='mostrar_imagenes'),
]