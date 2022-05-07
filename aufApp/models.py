from django.db import models

# Create your models here.

class Equipo(models.Model):
    nombre = models.CharField(max_length=50)
    direccionSede = models.CharField(max_length=75)
    email = models.EmailField()
    fechaCreacion = models.DateTimeField()
    
class Futbolista(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    fechaNacimiento = models.DateTimeField()

class Estadio(models.Model):
    direccion = models.CharField(max_length=75)
    nombre = models.CharField(max_length=50)
    fechaInauguracion = models.DateTimeField()
    propietario = models.CharField(max_length=50)
