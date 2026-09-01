from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
# Importa desde tu app, no desde el proyecto principal
from imagenes_app import views  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.pagina_principal, name='inicio'),
    path('subir/', views.subir_imagen, name='subir_imagen'),
    path('mostrar/', views.mostrar_imagenes, name='mostrar_imagenes'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)