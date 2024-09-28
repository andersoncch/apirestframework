from django.db import models

# Create your models here.
class Departamento(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    class Meta:
        db_table = 'departamento'  # Nombre de la tabla en la base de datos