from django.db import models

# Create your models here.

class MaterialesPractica(models.Model):
    id=models.AutoField(primary_key=True,verbose_name="Clave")
    nombrePractica=models.TextField()
    hora=models.CharField(max_length=15)
    solicitante=models.TextField()
    grupo=models.CharField(max_length=4)
    """material=ArrayField(
        ArrayField(
            models.TextField(max_length=100, blank=True),
            size=8,
        ),)"""

class Empleados(models.Model):
    id=models.AutoField(primary_key=True,verbose_name="Clave")
    foto = models.ImageField(null=True,upload_to="fotos",verbose_name="Fotografía")
    nombreEmpleado=models.TextField()
    skills=models.CharField(max_length=15)
    telefono=models.CharField(max_length=11)
    domicilio=models.TextField()

    class Meta:
        verbose_name = "Empleado"
        verbose_name_plural = "Empleados"
    
    def __str__(self):
        return self.nombreEmpleado