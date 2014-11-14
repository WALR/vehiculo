from django.db import models
from django.contrib.auth.models import User

class empleado (models.Model):
    usuario = models.OneToOneField(User)
    fecha_ingreso = models.DateField()
    telefono = models.IntegerField()
    direccion = models.CharField(max_length=70)
    categoria = models.ForeignKey("categoria")

    def __unicode__(self):
        return self.usuario.username


class categoria (models.Model):
    nombre = models.CharField(max_length=90, blank=False)
    salario = models.FloatField()


class vehiculo(models.Model):
    modelo = models.CharField(max_length=50)
    marcha = models.CharField(max_length=50)
    chasis = models.CharField(max_length=50)
    placa = models.CharField(max_length=50)
    color = models.CharField(max_length=50)


class localidad(models.Model):
    nombre = models.CharField(max_length=80)
    direccion = models.CharField(max_length=150)
    telefono = models.IntegerField()
    email = models.EmailField()

class ruta(models.Model):
    nombre = models.CharField(max_length=80)
    direccion = models.CharField(max_length=150)
    lugarincio = models.CharField(max_length=80)
    lugardestino = models.CharField(max_length=80)

class viaje(models.Model):
    vehiculo = models.ForeignKey(vehiculo)
    ruta = models.ForeignKey(ruta)
    empleado = models.ForeignKey(empleado)
    estado = models.BooleanField(default=False)


class incidencia(models.Model):
    viaje = models.ForeignKey(viaje)
    tipo = models.CharField(max_length=80)
    observacion = models.CharField(max_length=150)
    fecha = models.DateField()