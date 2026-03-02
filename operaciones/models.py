from django.db import models

# Create your models here.


class apartamentos(models.Model):
    apartamentoId = models.AutoField()
    numero = models.CharField(null=False, max_length=10)
    habitaciones = models.IntegerField(null=False)
    banios = models.IntegerField(null=False)
    estado = models.CharField(null=False, max_length=20, choices=[('disponible'),('ocupado'),('mantenimiento'),], default='disponible')
    fecha_reg = models.DateField(auto_now_add=True)
    def __str__(self):
        return f'Apartamento: {self.numero} [{self.estado}]'
    
class mantenimientos(models.Model):
    mantenimientosId = models.AutoField()
    descripcion = models.TextField(null=False)
    prioridad = models.CharField(null=False, max_length=20, choices=[('baja'),('media'),('alta'),], default='media')
    coste = models.DecimalField(null=False, max_digits=10, decimal_places=2)
    fecha = models.DateField(auto_now_add=True)
    estado = models.CharField(null=False, max_length=20, choices=[('pendiente'),('en progreso'),('completado'),], default='pendiente')
    responsable = models.CharField(null=True, max_length=30)
    def __str__(self):
        return f'Responsable: {self.responsable} | Mantenimiento: {self.descripcion}'

class contratos(models.Model):
    contratoId = models.AutoField()
    inquilinosId = models.ForeignKey('usuarios.inquilinos', on_delete=models.CASCADE, null=True)
    apartamentosId = models.ForeignKey('apartamentos.apartamentos', on_delete=models.CASCADE, null=True)
    fechaInicio = models.DateField(null=False)
    fechaFin = models.DateField(null=False)
    montoAlquiler = models.DecimalField(null=False, max_digits=10, decimal_places=2)
    deposito = models.DecimalField(null=False, max_digits=10, decimal_places=2)
    estado = models.CharField(null=False, max_length=20, choices=[('activo'),('terminado'),('cancelado'),], default='activo')
    def __str__(self):
        return f'Contrato: {self.contratoId} | Inquilino: {self.inquilinosId} | Apartamento: {self.apartamentosId}'