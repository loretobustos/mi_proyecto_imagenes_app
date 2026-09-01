from django.shortcuts import render, redirect
from .models import Imagen
from .forms import ImagenForm

def pagina_principal(request):
   return render(request, 'imagenes_app/mostrar_imagenes.html')

def subir_imagen(request):
    if request.method == 'POST':
        form = ImagenForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('mostrar_imagenes')
    else:
        form = ImagenForm()
    
    return render(request, 'imagenes_app/subir_imagen.html', {'form': form})  

def mostrar_imagenes(request):
    imagenes = Imagen.objects.all().order_by('-fecha_subida')
    return render(request, 'imagenes_app/mostrar_imagenes.html', {'imagenes': imagenes})  