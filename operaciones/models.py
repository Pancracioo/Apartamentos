from django.db import models


class Apartamento(models.Model):
    ESTADO = [
        ('disponible', 'Disponible'),
        ('ocupado', 'Ocupado'),
        ('mantenimiento', 'Mantenimiento'),
    ]
    apartamentoId = models.AutoField(primary_key=True)
    numero = models.CharField(max_length=10)
    habitaciones = models.IntegerField()
    banios = models.IntegerField()
    estado = models.CharField(max_length=20, choices=ESTADO, default='disponible')
    fecha_reg = models.DateField(auto_now_add=True)
    def __str__(self):
        return f'Apartamento {self.numero} [{self.estado}]'

class Mantenimiento(models.Model):
    PRIORIDAD = [
        ('baja', 'Baja'),
        ('media', 'Media'),
        ('alta', 'Alta'),
    ]
    ESTADO = [
        ('pendiente', 'Pendiente'),
        ('en progreso', 'En progreso'),
        ('completado', 'Completado'),
    ]
    mantenimientoId = models.AutoField(primary_key=True)
    descripcion = models.TextField()
    prioridad = models.CharField(max_length=20, choices=PRIORIDAD, default='media')
    coste = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateField(auto_now_add=True)
    estado = models.CharField(max_length=20, choices=ESTADO, default='pendiente')
    responsable = models.CharField(max_length=30, null=True, blank=True)
    def __str__(self):
        return f'{self.descripcion} | Responsable: {self.responsable}'

class Contrato(models.Model):
    ESTADO = [
        ('activo', 'Activo'),
        ('terminado', 'Terminado'),
        ('cancelado', 'Cancelado'),
    ]
    contratoId = models.AutoField(primary_key=True)
    inquilino = models.ForeignKey(
        'usuarios.Inquilino',
        on_delete=models.CASCADE,
        related_name='contratos'
    )
    apartamento = models.ForeignKey(
        'operaciones.Apartamento',
        on_delete=models.CASCADE,
        related_name='contratos'
    )
    fechaInicio = models.DateField()
    fechaFin = models.DateField()
    montoAlquiler = models.DecimalField(max_digits=10, decimal_places=2)
    deposito = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.CharField(max_length=20, choices=ESTADO, default='activo')
    def __str__(self):
        return f'Contrato {self.contratoId} | {self.inquilino}'