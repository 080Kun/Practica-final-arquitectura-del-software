from django.db import models

class Monitor(models.Model):
    nombre = models.CharField(max_length=100)
    numActividades = models.IntegerField(min=0)
    especializacioin = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre

class Actividad(models.Model):
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)
    horario = models.CharField(max_length=100)
    descripción = models.CharField(max_length=500)
    duración = models.IntegerField(min=15)
    plazas_disponibles = models.IntegerField(min=0)
    monitor = models.ForeignKey(Monitor, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.nombre}: {self.descripción}"


class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField(min=3)
    telefono = models.CharField(max_length=15)
    email = models.EmailField()
    def __str__(self):
        return self.nombre


class Sala(models.Model):
    nombre = models.CharField(max_length=100)
    capacidad = models.IntegerField(min=0)
    ubicacion = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre

