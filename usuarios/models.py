from django.db import models


class Usuario(models.Model):
    PERMISOS = [
        ('admin', 'Admin'),
        ('cobrador', 'Cobrador'),
        ('mantenimiento', 'Mantenimiento'),
    ]
    usuarioId = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    contrasenia = models.CharField(max_length=128)
    permisos = models.CharField(max_length=20, choices=PERMISOS, default='mantenimiento')
    fecha_nac = models.DateField(null=True, blank=True)
    fecha_reg = models.DateField(auto_now_add=True)
    def __str__(self):
        return f'{self.usuarioId} {self.nombre} [{self.permisos}]'


class Inquilino(models.Model):
    inquilinoId = models.AutoField(primary_key=True)
    apartamento = models.ForeignKey(
        'operaciones.Apartamento',
        on_delete=models.SET_NULL,
        null=True,
        related_name='inquilinos'
    )
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField(null=True, blank=True)
    tel = models.CharField(max_length=20, null=True, blank=True)
    cedula = models.CharField(max_length=20, null=True, blank=True)
    fecha_nac = models.DateField(null=True, blank=True)
    fecha_reg = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.nombre} {self.apellido}'