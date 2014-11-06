from django.db import models

class rutaInteres(models.Model):
    descripcion = models.TextField(max_length=200)
    direccion = models.CharField(max_length=60, blank=True)
    telefono = models.IntegerField(max_length=50, blank=True)
    email = models.EmailField(max_length=50, blank=True)
    fecha = models.DateField(max_length=50)
    estado = models.CharField(max_length=30)

    def __unicode__(self):
        return self.descripcion


