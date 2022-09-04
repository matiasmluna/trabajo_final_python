from django.db import models

# Create your models here.
class Familiares(models.Model):
    nombre= models.CharField(max_length=30)
    fechaDeNacimiento = models.DateField()
    edad = models.IntegerField()

class Profesiones(models.Model):
    profesion= models.CharField(max_length=30)
    sueldo = models.IntegerField()

class Articulos(models.Model):
    nombre_articulo= models.CharField(max_length=30)
    stock = models.IntegerField()
    precio = models.IntegerField()
