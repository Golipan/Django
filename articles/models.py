from django.db import models

# Create your models here.
class horario(models.Model):
    dirigente = models.TextField()
    sala = models.IntegerField()
    entidad = models.IntegerField()
    fecha = models.DateField()

class dirigente(models.Model):
    id_dirigente = models.IntegerField()
    nombre = models.TextField()

class sala(models.Model):
    url = models.URLField()
    id_sala = models.IntegerField()
    nombre = models.TextField()

class entidad(models.Model):
    id_entidad = models.IntegerField()
    Nombre = models.TextField()

