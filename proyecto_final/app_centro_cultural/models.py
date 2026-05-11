from django.db import models

class Monitor(models.Model):
    nombre = models.CharField(max_length=100)
    numActividades = models.IntegerField()
    especializacioin = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre
    
class Sala(models.Model):
    nombre = models.CharField(max_length=100)
    capacidad = models.IntegerField()
    ubicacion = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre

class Actividad(models.Model):
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)
    horario = models.CharField(max_length=100)
    descripción = models.CharField(max_length=500)
    duración = models.IntegerField()
    plazas_disponibles = models.IntegerField()
    monitor = models.ForeignKey(Monitor, on_delete=models.CASCADE)
    sala = models.ForeignKey(Sala, on_delete=models.CASCADE)
    def save(self, *args, **kwargs):
        nuevaActividad = self.pk is None

        super().save(*args, **kwargs)

        if nuevaActividad:
            self.monitor.numActividades += 1
            self.monitor.save()

    def __str__(self):
        return f"{self.nombre}: {self.descripción}"


class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()
    telefono = models.CharField(max_length=15)
    email = models.EmailField()
    def __str__(self):
        return self.nombre
    
class Inscripcion(models.Model):
    actividad=models.ForeignKey(Actividad, on_delete=models.CASCADE)
    usuario=models.ForeignKey(Usuario, on_delete=models.CASCADE)
    def save(self, *args, **kwargs):
        nuevaInscr = self.pk is None

        if nuevaInscr:
            if self.actividad.plazas_disponibles > 0:
                self.actividad.plazas_disponibles -= 1
                self.actividad.save()
            else:
                raise ValueError("No quedan plazas disponibles")

        super().save(*args, **kwargs)

