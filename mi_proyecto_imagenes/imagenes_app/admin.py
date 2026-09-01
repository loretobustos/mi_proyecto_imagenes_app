from django.contrib import admin
from .models import Imagen

@admin.register(Imagen)
class ImagenAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'fecha_subida']
    list_filter = ['fecha_subida']
    search_fields = ['titulo']
    readonly_fields = ['fecha_subida']
