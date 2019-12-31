from django.db import models

from app.persona.models import Empleado 

# Create your models here.+

class Corte(models.Model):
    nombre = models.CharField(max_length=70)
    decripcion = models.CharField(max_length=150, blank=True, null= True)
    precio = models.FloatField()

    def __str__(self):
        return '{}'.format(self.nombre)

class Tintura(models.Model):
    nombre = models.CharField(max_length=50)
    codigo = models.CharField(max_length=50)
    marca = models.CharField(max_length=50, blank=True, null=True)
    gramo = models.IntegerField(blank=True, null=True)
    precio = models.FloatField()

    def __str__(self):
        return '{}'.format(self.nombre)
        
class Color(Corte):
    
    codigo = models.CharField(max_length=50, blank= True, null=True)

    def __str__(self):
        return '{}'.format(self.nombre)

class Mano(models.Model):
    nombre = models.CharField(max_length=50, blank=True, null=True)
    concepto = models.CharField(max_length=70)
    precio = models.FloatField() 
    
    def __str__(self):
        return '{}'.format(self.concepto)

class Cabina(models.Model):
    concepto = models.CharField(max_length=70)
    precio = models.FloatField()
    contador = models.IntegerField()

    def __str__(self):
        return '{}'.format(self.concepto)

