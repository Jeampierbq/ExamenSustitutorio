from django.db import models

# Create your models here.
from django.db import models

class Barrios_Usuarios(models.Model):
    DISPONIBILIDAD = [
        ('A', 'Activado'),
        ('D', 'Desactivado'),
    ]
    
    Barrios_login = models.CharField(max_length=100)
    Barrios_clave = models.CharField(max_length=100)
    Barrios_disponible = models.CharField(max_length=1, choices=DISPONIBILIDAD, default='A')
    Barrios_fecha_de_registro = models.DateTimeField(auto_now_add=True)
