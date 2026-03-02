from django.db import models

# Create your models here.
class usuarios(models.Model):
    usuarioId = models.AutoField()
    nombre = models.CharField(null=False, max_length=50)
    contrasenia = models.CharField(null=False, max_length=128)
    permisos = models.CharField(null=False, max_length=20, choices=[('admin'),('cobrador'),('mantenimiento'),], default='mantenimiento')
    fecha_nac = models.DateField(null=True)
    fecha_reg = models.DateField(auto_now_add=True)
    def __str__(self):
        return f'{self.usuarioId} {self.nombre} [{self.permisos}]'

class inquilinos(models.Model):
    inquilinoId = models.AutoField()
    nombre = models.CharField(null=False, max_length=50)
    apellido = models.CharField(null=False, max_length=50)
    email = models.models.EmailField(null=True, max_length=254)
    tel = models.models.PhoneNumberField(null=True)
    cedula = models.CharField(null=True, max_length=20)
    apartamentosId = models.ForeignKey('apartamentos.apartamentos', on_delete=models.CASCADE, null=True)
    fecha_nac = models.DateField(null=True)
    fecha_reg = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.nombre + ' ' + self.apellido
