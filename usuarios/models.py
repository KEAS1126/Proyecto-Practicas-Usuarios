from django.db import models


# Create your models here.

class Usuarios(models.Model):
    idUsuario = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=60)
    correo = models.EmailField()
    celular = models.CharField(max_length=10)
    ciudad = models.CharField(max_length=60)
    contrasena = models.CharField(max_length=60)
    imagen=models.ImageField(upload_to="imgUsuario", null=True)

