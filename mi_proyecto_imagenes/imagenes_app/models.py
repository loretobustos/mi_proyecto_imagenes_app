from django.db import models

class Imagen(models.Model):
    titulo = models.CharField(max_length=100, verbose_name="Título de la imagen")
    imagen = models.ImageField(upload_to='imagenes/', verbose_name="Seleccionar imagen")
    fecha_subida = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de subida")

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = "Imagen"
        verbose_name_plural = "Imágenes"
