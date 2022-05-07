from django.db import models

class Futbolista(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    email= models.EmailField()
    fechaNacimiento = models.DateField()
    
    def __str__(self):
        return self.nombre + " " + self.apellido

class Equipos(models.Model):
    nombre= models.CharField(max_length=30)
    direccionSede = models.CharField(max_length=30)
    email= models.EmailField()
    fechaFundacion = models.DateField()
    
    def __str__(self):
        return self.nombre + " " + str(self.fechaFundacion)

class Estadio(models.Model):
    nombre= models.CharField(max_length=30)
    direccion = models.CharField(max_length=50)  
    fechaConstruccion = models.DateField()
    propietario = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombre + " " + self.direccion
