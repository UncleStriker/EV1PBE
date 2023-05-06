from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()

class Vehiculo(models.Model):
    Anno = models.DateField()
    Marca = models.CharField(max_length=255)
    Color = models.CharField(max_length=255)
    Combustible = models.CharField(max_length=255)
    NumPuertas = models.IntegerField()
    Traccion = models.CharField(max_length=255)