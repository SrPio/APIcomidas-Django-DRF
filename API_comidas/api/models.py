from django.db import models

# Create your models here.
class Alimento(models.Model):
    nombre=models.CharField(max_length=50)
    categoria=models.CharField(max_length=20)
    
    def __str__(self):
        return self.nombre

class Plato(models.Model):
    nombre=models.CharField(max_length=50)
    tiempo=models.CharField(max_length=360)
    categoria=models.CharField(max_length=20)
    alimento= models.ManyToManyField(Alimento)

    def __str__(self):
        return self.nombre