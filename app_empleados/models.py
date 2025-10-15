from django.db import models

class Empleado(models.Model):
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=100)
    edad = models.IntegerField()
    correo = models.EmailField(max_length=100)
    numero_telefono = models.CharField(max_length=15) # Ajustado a 15 para más flexibilidad

    def __str__(self):
        return f'Empleado: {self.nombre} {self.apellidos}'