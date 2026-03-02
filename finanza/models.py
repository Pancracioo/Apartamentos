from django.db import models

# Create your models here.

class pagos(models.Model):
    pagoId = models.AutoField()
    contratoId = models.ForeignKey('operaciones.contratos', on_delete=models.CASCADE, null=True)
    metodo = models.CharField(null=False, max_length=20, choices=[('efectivo'),('tarjeta'),('transferencia'),], default='efectivo')
    montoTotal = models.DecimalField(null=False, max_digits=10, decimal_places=2)
    periodo = models.CharField(null=False, max_length=20)
    estado = models.CharField(null=False, max_length=20, choices=[('pendiente'),('pagado'),('atrasado'),], default='pendiente')
    def __str__(self):
        return f'Pago: {self.pagoId} | Contrato: {self.periodo} | Monto: {self.montoTotal} | Estado: {self.estado}'
    
class gastos(models.Model):
    gastoId = models.AutoField()
    descripcion = models.TextField(null=False)
    fecha = models.DateField(auto_now_add=True)
    coste = models.DecimalField(null=False, max_digits=10, decimal_places=2)
    periodo = models.CharField(null=False, max_length=20)
    estado = models.CharField(null=False, max_length=20, choices=[('pendiente'),('pagado'),('atrasado'),], default='pendiente')
    def __str__(self):
        return f'Gasto: {self.descripcion} | Monto: {self.coste} | Fecha: {self.fecha}'
    
class gastos_apartamento(models.Model):
    gastos_apartamentoId = models.AutoField()
    gastoId = models.ForeignKey('gastos', on_delete=models.CASCADE, null=True)
    apartamentoId = models.ForeignKey('operaciones.apartamentos', on_delete=models.CASCADE, null=True)
    monto_asignado = models.DecimalField(null=False, max_digits=10, decimal_places=2)
    coste = models.DecimalField(null=False, max_digits=10, decimal_places=2)
    pagoEstado = models.CharField(null=False, max_length=20, choices=[('pendiente'),('pagado'),('atrasado'),], default='pendiente')
    def __str__(self):
        return f'Gasto: {self.gastoId} | Apartamento: {self.apartamentoId} | Monto Asignado: {self.monto_asignado} | Pago Estado: {self.pagoEstado}'
